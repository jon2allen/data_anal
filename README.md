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


