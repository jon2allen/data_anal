import pandas as pd
import pandasai as pai
import litellm
from pandasai_litellm.litellm import LiteLLM
from dotenv import load_dotenv
import os
import argparse
import re

def main():
    """
    Main function to parse arguments and run the data analysis workflow.
    """
    # --- 1. ARGUMENT PARSING ---
    parser = argparse.ArgumentParser(
        description="A CLI tool to analyze CSV data using PandasAI and LiteLLM.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "csv_file",
        help="Path to the CSV file to be analyzed."
    )
    parser.add_argument(
        "--role",
        type=str,
        default="a curious data analyst",
        help="Specify the persona for generating questions (e.g., 'a financial analyst', 'a marketing director')."
    )
    parser.add_argument(
        "--questions",
        type=int,
        default=6,
        help="The number of questions to generate about the data."
    )
    parser.add_argument(
        "--report",
        type=str,
        help="Optional. Path to a text file to save the full output report."
    )
    parser.add_argument(
        "--qfile",
        type=str,
        help="Optional. Path to a text file to save only the generated questions."
    )
    parser.add_argument(
        "--execute",
        action="store_true", # This makes it a flag, e.g., --execute
        help="If specified, execute the generated questions against the data using PandasAI."
    )
    args = parser.parse_args()

    # --- 2. ENVIRONMENT AND LLM SETUP ---
    load_dotenv()
    if "GEMINI_API_KEY" not in os.environ:
        print("ERROR: GEMINI_API_KEY not found. Please set it in your environment or a .env file.")
        return

    # Use a clear variable name for the PandasAI wrapper instance
    llm = LiteLLM(model="gemini/gemini-2.5-flash")

    # Use a list to buffer all output for final reporting
    output_buffer = []


    # Configure PandasAI to use this LLM
    pai.config.set({
        "llm": llm,
        "save_logs": False,
        "verbose": False,
        "max_retries": 5 
    })


    try:
        # --- 3. DATA LOADING AND INITIAL DESCRIPTION ---
        print(f"-> Loading data from '{args.csv_file}'...")
        df = pai.read_csv(args.csv_file)

        print("-> Getting initial data description from PandasAI...")
        data_description = df.chat("Give a concise description of the data, including column names and a brief summary.")
        
        output_buffer.append("--- DATA DESCRIPTION --- \n\n")
        output_buffer.append(data_description)
        output_buffer.append("\n" + "="*50 + "\n")
        print(data_description)

        # --- 4. GENERATE QUESTIONS WITH LITELLM ---
        print(f"-> Asking Gemini to generate {args.questions} questions...")
        prompt_for_gemini = (
            f"You are {args.role}. Based on the data description below, "
            f"generate exactly {args.questions} insightful questions to ask about the data. "
            f"Output only the questions, one per line, without any numbering, commentary, or introduction.\n\n"
            f"Data Description:\n{data_description}"
        )
        
        response = litellm.completion(
            model="gemini/gemini-2.5-flash",
            messages=[{"role": "user", "content": prompt_for_gemini}]
        )
        print("checking response" )        
        generated_questions_text = response.choices[0].message.content
        print(generated_questions_text)
        generated_questions_text = str(generated_questions_text)
        # Clean up the list of questions (remove empty lines)
        question_list = [q.strip() for q in generated_questions_text.strip().split('\n') if q.strip()]
        print("processed questions")  
        output_buffer.append(f"--- GENERATED QUESTIONS (as {args.role.upper()}) ---\n")
        for i, question  in enumerate(question_list):
           output_buffer.append( str(i+1) + ": "+ question + " \n")
        #output_buffer.extend(question_list)
        #output_buffer.extend( generated_questions_text)
        
        print("print questoins")
        # --- 5. SAVE QUESTIONS TO QFILE (IF REQUESTED) ---
        if args.qfile:
            print(f"-> Saving generated questions to '{args.qfile}'...")
            with open(args.qfile, 'w') as f:
                f.write("\n".join(question_list))
            print(f"   Successfully saved questions.")

        # --- 6. EXECUTE QUESTIONS (IF REQUESTED) ---
        if args.execute:
            print(f"-> Executing {len(question_list)} questions with PandasAI...")
            output_buffer.append("\n" + "="*50 + "\n")
            output_buffer.append("--- PANDASAI ANSWERS ---")
            for i, question in enumerate(question_list):
                print(f"   Executing question {i+1}/{len(question_list)}: \"{question}\"")
                try:
                    answer = df.chat(question)
                    output_buffer.append(f"\nQ: {question}")
                    output_buffer.append(f"\nA: \n {str(answer)} \n")
                except Exception as e:
                    output_buffer.append(f"\nQ: {question}")
                    output_buffer.append(f"\nA: ERROR - Could not execute this question. Reason: {e}")
        
        # --- 7. FINAL OUTPUT ---
        print("final1")
        final_report = output_buffer
        print("type:  ", type(output_buffer) )
        print("final2")
        if args.report:
            print(f"-> Writing full report to '{args.report}'...")
            with open(args.report, 'w') as f:
                for i in final_report:
                   f.write(str(i))
            print("-> Done.")
        else:
            print("\n" + "="*50)
            print("--- FINAL REPORT ---")
            for i in final_report:
                print(i)
            print("="*50)


    except FileNotFoundError:
        print(f"ERROR: The file '{args.csv_file}' was not found.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

