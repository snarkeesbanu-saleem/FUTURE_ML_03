import streamlit as st
import pandas as pd
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pdfplumber
from docx import Document
import spacy
import nltk
from nltk.corpus import stopwords
from datetime import datetime
from io import BytesIO

# ── Setup (same as notebook) ───────────────────────────────────────
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

# ── Functions (copied & slightly adapted from your notebook) ───────
def extract_resume_text(file_content, ext):
    text = ""
    try:
        if ext == '.pdf':
            with pdfplumber.open(BytesIO(file_content)) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        elif ext == '.docx':
            doc = Document(BytesIO(file_content))
            for para in doc.paragraphs:
                if para.text.strip():
                    text += para.text + "\n"
        return text.strip()
    except:
        return ""

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = [w for w in text.split() if w not in stop_words and len(w) > 2]
    return ' '.join(words)

def extract_keywords(text):
    if not text:
        return []
    doc = nlp(text.lower())
    keywords = set()
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'GPE', 'DATE', 'NORP', 'PRODUCT']:
            keywords.add(ent.text.strip())
    skill_patterns = r'(python|java|sql|machine learning|deep learning|nlp|tensorflow|pytorch|scikit-learn|pandas|numpy|aws|azure|git|docker|communication|leadership|teamwork|financial advisor|investment|portfolio management|graphic design|illustrator|photoshop|indesign|figma|framer|procreate|adobe creative suite|ms office)'
    found = re.findall(skill_patterns, text.lower())
    keywords.update(found)
    return sorted(list(set(keywords)))

# ── Streamlit App ──────────────────────────────────────────────────
st.set_page_config(page_title="Resume Ranker – Future Interns Task 3", layout="wide")

st.title("AI Resume Screener & Candidate Ranker")
st.markdown("Upload resumes (.docx / .pdf) and paste a job description to rank candidates by fit.")

# ── Inputs ─────────────────────────────────────────────────────────
job_desc = st.text_area("Job Description", height=200,
                        placeholder="Paste the job description here (skills, requirements, etc.)")

uploaded_files = st.file_uploader("Upload Resumes", type=["docx", "pdf"], accept_multiple_files=True)

if st.button("Rank Candidates") and job_desc and uploaded_files:
    with st.spinner("Processing resumes..."):
        data = []
        
        for file in uploaded_files:
            file_content = file.read()
            ext = os.path.splitext(file.name)[1].lower()
            raw_text = extract_resume_text(file_content, ext)
            
            if raw_text:
                clean = clean_text(raw_text)
                skills = extract_keywords(raw_text)
                years = 0  # simple placeholder - can improve later
                edu = "Unknown"  # can parse better later
                
                data.append({
                    'filename': file.name,
                    'clean_text': clean,
                    'skills': ', '.join(skills),
                    'years_exp': years,
                    'education': edu
                })
        
        if not data:
            st.error("No text could be extracted from uploaded files. Try different resumes or check file format.")
        else:
            df = pd.DataFrame(data)
            
            # Job description processing
            job_clean = clean_text(job_desc)
            
            # TF-IDF + similarity
            all_texts = [job_clean] + df['clean_text'].tolist()
            vectorizer = TfidfVectorizer(max_features=8000, ngram_range=(1,2), stop_words='english')
            tfidf = vectorizer.fit_transform(all_texts)
            sim_scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten() * 100
            
            # Weighted final score
            df['final_score'] = sim_scores.round(2)
            
            # Rank
            df = df.sort_values('final_score', ascending=False).reset_index(drop=True)
            df['rank'] = df.index + 1
            
            # Display
            st.success(f"Ranked {len(df)} candidates!")
            st.dataframe(df[['rank', 'filename', 'final_score', 'skills']])
            
            # Download CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Ranked Results (CSV)",
                data=csv,
                file_name="candidate_ranking.csv",
                mime="text/csv"
            )

st.markdown("---")
st.caption("Built for Future Interns ML Internship – Task 3 | Uses spaCy, pdfplumber, python-docx, scikit-learn")