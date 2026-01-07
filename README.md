# Resume-Analyser-using-python

USING GOOGLE COLLAB

# 1. Introduction
In today’s competitive job market, organizations receive a large number of resumes for each job opening. Manually screening these resumes is time-consuming, inefficient, and prone to human bias. To overcome these challenges, automation using Artificial Intelligence (AI) and Natural Language Processing (NLP) has become essential.
This project presents an AI Resume Analyzer that automatically analyzes resumes provided as PDF links and matches them with a given job description. The system helps evaluate candidate suitability efficiently using NLP and machine learning techniques.

# 2. Problem Statement
Manual resume screening requires significant human effort and time. Recruiters may unintentionally overlook suitable candidates or introduce bias during evaluation. Additionally, handling resumes in different formats makes the process complex.
Therefore, there is a need for an automated system that can:
Read resumes automatically
Extract relevant skills
Match resumes with job requirements
Provide an objective evaluation score

# 3. Objectives of the Project
The main objectives of this project are:
To analyze resumes automatically using AI techniques
To extract key technical skills from resumes
To compare resumes with job descriptions
To calculate a resume–job matching score
To reduce manual effort in resume screening

# 4. Use Case
This system can be used by:
HR departments for initial resume screening
Recruitment agencies
Educational institutions for placement evaluation
Individuals to evaluate their resumes against job roles

# 5. AI Approach and Methodology
The project uses Natural Language Processing (NLP) and Machine Learning (ML) techniques to analyze text data.

Methodology:
Resume is provided as a PDF link
Text is extracted from the PDF using PyPDF2
Text preprocessing is performed (lowercasing, punctuation removal)
TF-IDF (Term Frequency–Inverse Document Frequency) converts text into numerical vectors
Cosine Similarity measures similarity between resume and job description
A matching score is generated
Skills are extracted using keyword matching

# 6. Tools and Technologies Used
Programming Language: Python
Platform: Google Colab / PyCharm

Libraries Used:
NLTK – NLP processing
Scikit-learn – Machine learning algorithms
PyPDF2 – PDF text extraction
Requests – Fetching online PDF files

# 7. Output and Results
The system generates the following outputs:
List of extracted skills from the resume
Resume–job matching score (in percentage)
Suitability classification:
Strong Match
Moderate Match
Weak Match

The system works efficiently in Google Colab and PyCharm without requiring any API key.


Final output displays score and suitability status
