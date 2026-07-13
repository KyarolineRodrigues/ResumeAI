from fastapi import FastAPI, UploadFile, File
import os
import shutil

from app.resume_parser import extract_text


app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "ResumeAI is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    upload_dir = "uploads"

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    return {
        "filename": file.filename,
        "text": text
    }