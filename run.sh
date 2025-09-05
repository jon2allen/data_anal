#!/bin/bash

# Example 1: Generate 3 questions as a financial analyst and save the questions to a file
echo "Running Example 1: Generate 3 questions as a financial analyst..."
python3 data_anal.py cayuga.csv --role "a financial analyst" --questions 3 --qfile generated_questions.txt

# Example 2: Load pre-written questions from a file and execute them, saving the full report
echo "Running Example 2: Load questions from q1.txt and execute, saving the report..."
python3 data_anal.py cayuga.csv --qload q1.txt --execute --report analysis_report.txt

echo "Both examples completed. Check generated_questions.txt and analysis_report.txt for results."

