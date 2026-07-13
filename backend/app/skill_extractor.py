SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "express",
    "fastapi",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "power bi",
    "excel",
    "tableau",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))