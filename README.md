# Data Analysis with PandasAI and Gemini

**A Python tool for analyzing CSV data using PandasAI and Gemini.**

---

## Overview

This repository provides a simple framework for performing data analysis on CSV files using [PandasAI](https://github.com/Sinaptik-AI/pandas-ai) and [Gemini](https://deepmind.google/technologies/gemini/). It is designed to help users quickly load, analyze, and extract insights from their datasets with minimal setup.

---

## Features

- Load and analyze CSV files using natural language queries.
- Leverage the power of PandasAI for intuitive data manipulation.
- Generate questions about your data based on a specified role.
- Execute questions and save reports.
- Sample datasets included for testing and demonstration.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Required Python packages (see `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jon2allen/data_anal.git
   cd data_anal
   '''

### Running

   ```
   usage: data_anal.py [-h] [--role ROLE] [--questions QUESTIONS] [--report REPORT] [--qfile QFILE] [--qload QLOAD] [--execute]
                    csv_file

A CLI tool to analyze CSV data using PandasAI and LiteLLM.

positional arguments:
  csv_file              Path to the CSV file to be analyzed.

options:
  -h, --help            show this help message and exit
  --role ROLE           Specify the persona for generating questions (e.g., 'a financial analyst', 'a marketing director').
  --questions QUESTIONS
                        The number of questions to generate about the data.
  --report REPORT       Optional. Path to a text file to save the full output report.
  --qfile QFILE         Optional. Path to a text file to save only the generated questions.
  --qload QLOAD         Optional. Path to a text file with pre-written questions (one per line). Overrides --questions.
  --execute             If specified, execute the generated questions against the data using PandasAI.
```

## API Key Requirements for PandasAI with LiteLLM

This repository uses PandasAI and LiteLLM, which can interface with various large language models (LLMs) like Mistral, Google Gemini, or OpenAI.

Change this line in code:

```
    # Use a clear variable name for the PandasAI wrapper instance
    llm = LiteLLM(model="gemini/gemini-2.5-flash")
```

---

## API Key Requirements

| Provider  | Environment Variable      | Where to Get the Key                     |
|-----------|---------------------------|------------------------------------------|
| Mistral   | `MISTRAL_API_KEY`         | [Mistral AI Dashboard](https://mistral.ai/) |
| Gemini    | `GEMINI_API_KEY`          | [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key) |
| OpenAI    | `OPENAI_API_KEY`          | [OpenAI Platform](https://platform.openai.com/) |

---

## How to Set Up API Keys

### Mistral AI
- Sign up at [Mistral AI](https://mistral.ai/).
- Generate your API key from the dashboard.
- Set the environment variable:
  ```bash
  export MISTRAL_API_KEY="your-mistral-api-key"
  ```

### Google Gemini
- Get your key from [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key).
- Set the environment variable:
  ```bash
  export GEMINI_API_KEY="your-gemini-api-key"
  ```

### OpenAI
- Sign up at [OpenAI](https://platform.openai.com/).
- Generate your API key.
- Set the environment variable:
  ```bash
  export OPENAI_API_KEY="your-openai-api-key"
  ```

---

## Example Usage with LiteLLM and PandasAI

If your `data_anal.py` script uses LiteLLM, you can specify the model and API key in your code or via environment variables.

### Using Mistral
```python
from pandasai import SmartDataframe
from pandasai_litellm.litellm import LiteLLM

# Initialize LiteLLM with Mistral
llm = LiteLLM(model="mistral/mistral-tiny", api_key="your-mistral-api-key")
```


Or, set the environment variable and let LiteLLM handle the rest:
```bash
export MISTRAL_API_KEY="your-mistral-api-key"
python data_anal.py your_data.csv --role "a financial analyst" --questions 3
```

---

## Notes
- Always keep your API keys secure and never commit them to version control.
- The specific model name (e.g., `mistral/mistral-tiny`, `mistral/mistral-small`, etc.) depends on the Mistral model you want to use. Check the [LiteLLM documentation](https://docs.litellm.ai/) for supported models and exact names.
- If you switch between providers, just change the environment variable and model name in your script or command line.



