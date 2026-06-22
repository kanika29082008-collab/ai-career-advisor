import pdfplumber
import spacy
import json

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def preprocess_resume(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]
    return tokens

def extract_entities(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        entities.setdefault(ent.label_, []).append(ent.text)
    return entities

def extract_skills(text):
    skill_keywords = [
        # Technical
        "python", "java", "c++", "sql", "nlp", "machine learning",
        "deep learning", "tensorflow", "pytorch", "data analysis",
        "excel", "power bi", "tableau", "cloud", "aws", "azure",
        "git", "docker", "kubernetes",

        # Soft skills
        "communication", "teamwork", "leadership", "problem solving",
        "critical thinking", "adaptability", "creativity",
        "time management", "collaboration",

        # Domain-specific
        "project management", "business analysis", "marketing",
        "sales", "customer service", "research", "design"
    ]
    text_lower = text.lower()
    found_skills = [skill for skill in skill_keywords if skill in text_lower]
    return found_skills

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("C:/Users/Kanika/Desktop/ipr.pdf")

    tokens = preprocess_resume(resume_text)
    entities = extract_entities(resume_text)
    skills = extract_skills(resume_text)

    profile = {
        "raw_text_preview": resume_text[:500],
        "tokens_sample": tokens[:50],
        "entities": entities,
        "skills": skills
    }

    print("=== Structured Resume Profile ===")
    print(json.dumps(profile, indent=4))
def match_job_description(resume_skills, job_text):
    job_skills = extract_skills(job_text)
    matched = [skill for skill in job_skills if skill in resume_skills]
    missing = [skill for skill in job_skills if skill not in resume_skills]
    fit_score = round(len(matched) / len(job_skills) * 100, 2) if job_skills else 0

    return {
        "job_skills": job_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "fit_score": f"{fit_score}%"
    }

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("C:/Users/Kanika/Desktop/ipr.pdf")
    skills = extract_skills(resume_text)

    # Example job description (replace with real one)
    job_text = """
    We are looking for a Data Science Intern with skills in Python, SQL,
    Machine Learning, Deep Learning, TensorFlow, and good communication skills.
    """
    job_match = match_job_description(skills, job_text)

    print("\n=== Job Match Analysis ===")
    print(json.dumps(job_match, indent=4))
def match_job_description(resume_skills, job_text):
    job_skills = extract_skills(job_text)
    matched = [skill for skill in job_skills if skill in resume_skills]
    missing = [skill for skill in job_skills if skill not in resume_skills]
    fit_score = round(len(matched) / len(job_skills) * 100, 2) if job_skills else 0

    return {
        "job_skills": job_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "fit_score": f"{fit_score}%"
    }

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("C:/Users/Kanika/Desktop/ipr.pdf")
    skills = extract_skills(resume_text)

    # Example job description (replace with real one)
    job_text = """
    We are looking for a Data Science Intern with skills in Python, SQL,
    Machine Learning, Deep Learning, TensorFlow, and good communication skills.
    """
    job_match = match_job_description(skills, job_text)

    print("\n=== Job Match Analysis ===")
    print(json.dumps(job_match, indent=4))
