from app.resume_parser import extract_text

def extract_job_description(pdf_path):
    return extract_text(pdf_path)