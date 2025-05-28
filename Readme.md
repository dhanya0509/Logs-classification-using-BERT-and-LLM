# Log Classification Project

This project implements log message classification using both BERT embeddings and LLM approaches.

## Project Description
A Python-based system for classifying log messages into different categories using:
- BERT embeddings with SentenceTransformer
- Large Language Models integration
- Machine learning classification

## Setup and Installation

### Prerequisites
- Python 3.13.2
- Virtual environment (virtualenv)

### Installation Steps
1. Clone the repository:
```
bash git clone <repository-url> cd Classification_Logs
```

2. Create and activate virtual environment:
```
bash python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install sentence-transformers scikit-learn joblib groq python-dotenv
```
```
## Project Structure
```
Classification_Logs/
├── .venv/                  # Virtual environment directory
├── processor.bert.py       # BERT-based classification implementation
├── processor_llm.py        # LLM-based classification implementation
├── log_classifier.joblib   # Saved classifier model
└── README.md              # This file
```
## Usage
The project provides two different approaches for log classification:
### BERT-based Classification
``` python
python processor.bert.py
```
### LLM-based Classification
``` python
python processor_llm.py
```
## Environment Variables
Create a `.env` file in the project root with:
```
GROQ_API_KEY=your_api_key_here
```
## Features
- Log message classification using BERT embeddings
- Alternative classification using Large Language Models
- Support for multiple log formats
- Extensible classification categories

## Dependencies
- sentence-transformers
- scikit-learn
- joblib
- groq
- python-dotenv
- numpy
- pandas
