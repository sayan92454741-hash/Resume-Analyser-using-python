import nltk
import string
import requests
import PyPDF2
from io import BytesIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
cv_pdf_url = "https://drive.google.com/file/d/1mCogOS562zWhZuTjzpfF-0jOXxc5mHhn/view?usp=sharing"

def extract_text_from_pdf(url):
    response = requests.get(url)
    pdf_file = BytesIO(response.content)
    reader = PyPDF2.PdfReader(pdf_file)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text
job_description = """
Looking for a candidate with computer knnowledge, strong coding like python and other, good communication skill and talk multi language
"""
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text
def resume_matcher(resume, job_desc):
    documents = [preprocess(resume), preprocess(job_desc)]
    vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = round(similarity[0][0] * 100, 2)
    return score
skills_list = [
    "python", "coding", "deep learning", "ai", "computer knowledge"
    "drawing", "electronics", "languages(bengali, hindi, english)"
]

def extract_skills(resume):
    resume = preprocess(resume)
    extracted = [skill for skill in skills_list if skill in resume]
    return extracted

import nltk
nltk.download('punkt_tab')

cv_pdf_url = "https://drive.google.com/uc?export=download&id=1mCogOS562zWhZuTjzpfF-0jOXxc5mHhn"
resume_text = extract_text_from_pdf(cv_pdf_url)

score = resume_matcher(resume_text, job_description)
skills = extract_skills(resume_text)

print("📄 Resume Analyzer Result")
print("-------------------------")
print("✅ Extracted Skills:", skills)
print("📊 Resume Match Score:", score, "%")

if score >= 50:
    print("🎯 Status: Strong match for the job role")
elif score >=30:
    print("⚠️ Status: Moderate match – improvement needed")
else:
    print("❌ Status: Weak match – significant improvement needed")
