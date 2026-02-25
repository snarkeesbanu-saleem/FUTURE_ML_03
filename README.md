# FUTURE_ML_03 – AI Resume Screening & Candidate Ranking System

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![pdfplumber](https://img.shields.io/badge/pdfplumber-PDF-FF6F00?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](https://github.com/jsvine/pdfplumber)
[![python-docx](https://img.shields.io/badge/python--docx-DOCX-2B579A?style=for-the-badge&logo=microsoft-word&logoColor=white)](https://python-docx.readthedocs.io/)



An intelligent, end-to-end **resume screening and candidate ranking system** that helps recruiters quickly identify the best-fit candidates by:
- Parsing resumes in multiple formats (.docx, .pdf, .txt)
- Extracting key information (skills, estimated experience years, education level)
- Matching against a job description using TF-IDF + cosine similarity
- Computing a weighted final score (skills 60%, experience 25%, education 15%)
- Ranking candidates with explainable results

This project builds an intelligent resume parser and ranking system that:
- Reads resumes (.docx, .pdf, .txt)
- Extracts skills, estimated experience years, education
- Matches against a job description using TF-IDF + cosine similarity
- Ranks candidates with weighted final score (skills 60%, experience 25%, education 15%)

## Demo Results (with sample resumes)

**Ranked Candidates**

| Rank | Filename                          | Final Score | Key Skills (partial)                                      | Years Exp | Education |
|------|-----------------------------------|-------------|-----------------------------------------------------------|-----------|-----------|
| 1    | richard_financial.docx            | 11.27       | financial advisor, portfolio management, investment, ROI... | 0         | Bachelor  |
| 2    | aparna_graphic.docx               | 10.94       | graphic design, illustrator, photoshop, figma...          | 0         | Bachelor  |

Full results saved in `candidate_ranking.csv`

## How to Run

1. Place resume files (.docx/.pdf/.txt) in `resumes/` folder
2. Edit `sample_job_description.txt` (optional)
3. Run `resume_screening.ipynb`
4. View ranked table in console and CSV file

## Tech Stack
- Python, pandas, numpy, scikit-learn
- Text extraction: pdfplumber + python-docx
- NLP: spaCy (en_core_web_sm)
- Similarity: TF-IDF + cosine


Built with Python, spaCy, pdfplumber, python-docx, scikit-learn, and Streamlit.
