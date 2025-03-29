from flask import Flask, render_template, request, jsonify
import pandas as pd
from PyPDF2 import PdfReader
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import docx
import os
import io

app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def process_text(text):
    doc = nlp(text.lower())
    # Extract relevant information using spaCy
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

def calculate_similarity(job_desc, resume_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([job_desc, resume_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return similarity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        job_description = request.form['job_description']
        files = request.files.getlist('resumes')
        
        if not job_description or not files:
            return jsonify({'error': 'Missing job description or resume files'}), 400

        processed_job_desc = process_text(job_description)
        results = []

        for file in files:
            if file.filename == '':
                continue

            try:
                if file.filename.endswith('.pdf'):
                    resume_text = extract_text_from_pdf(file)
                elif file.filename.endswith('.docx'):
                    resume_text = extract_text_from_docx(file)
                else:
                    continue

                processed_resume = process_text(resume_text)
                similarity_score = calculate_similarity(processed_job_desc, processed_resume)

                results.append({
                    'filename': file.filename,
                    'score': similarity_score,
                    'preview': resume_text[:200] + "..."  # Short preview of resume
                })

            except Exception as e:
                print(f"Error processing {file.filename}: {str(e)}")
                continue

        # Sort results by score in descending order
        results.sort(key=lambda x: x['score'], reverse=True)
        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
