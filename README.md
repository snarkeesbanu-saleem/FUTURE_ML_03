# FUTURE_ML_03 – AI Resume Screening & Candidate Ranking System

**Task 3** of Future Interns Machine Learning Internship

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

## Note
- Scores are low due to mixed job description (ML + design + financial). Real use case would use focused JD.
- Experience detection is heuristic — can be improved with better date parsing.

Built for Future Interns ML Internship – Task 3
