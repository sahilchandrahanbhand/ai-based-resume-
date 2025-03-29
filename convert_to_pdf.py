from fpdf import FPDF
import os

def text_to_pdf(txt_file, pdf_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    with open(txt_file, 'r', encoding='utf-8') as file:
        for line in file:
            pdf.cell(0, 10, txt=line.strip(), ln=True)
    
    pdf.output(pdf_file)

# Convert all text files in sample_resumes to PDF
sample_dir = "sample_resumes"
for file in os.listdir(sample_dir):
    if file.endswith(".txt"):
        txt_path = os.path.join(sample_dir, file)
        pdf_path = os.path.join(sample_dir, file.replace(".txt", ".pdf"))
        text_to_pdf(txt_path, pdf_path)
