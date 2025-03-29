# AI-Based Resume Ranker

A modern web application that uses AI to rank resumes based on job descriptions.

## Features

- Resume Upload: Support for multiple PDF and DOCX files
- Text Extraction: NLP-based extraction of relevant data
- Job Description Parsing: AI-powered requirement extraction
- Skill & Experience Matching: Advanced text similarity matching
- Scoring & Ranking: Automated resume ranking based on relevance
- Dashboard Display: Interactive UI showing top candidates with match scores

## Installation

1. Clone this repository
2. Install the requirements:
```bash
pip install -r requirements.txt
```
3. Download the spaCy model:
```bash
python -m spacy download en_core_web_sm
```

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL
3. Enter the job description in the sidebar
4. Upload multiple resumes (PDF or DOCX format)
5. View the ranked results with match scores

## Technical Details

- Built with Python and Streamlit
- Uses spaCy for Natural Language Processing
- Implements TF-IDF and Cosine Similarity for matching
- Supports PDF and DOCX file formats
