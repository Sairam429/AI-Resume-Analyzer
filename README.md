# 🤖 AI Resume Analyzer & Job Recommendation System

An AI-powered web application that analyzes resumes, extracts skills, calculates resume-job compatibility, identifies missing skills, and recommends suitable jobs.

## 🚀 Features

* 📄 Upload resume in PDF format
* 🧠 Extract relevant skills from resumes
* 📊 Calculate resume/job match score
* 🥧 Display resume score using a pie chart
* ⚠️ Identify missing skills
* 🎯 Recommend suitable jobs
* 📈 Rank jobs using TF-IDF and Cosine Similarity
* 🌐 Interactive Streamlit web application

## 🛠️ Technologies

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* PDFPlumber
* Plotly
* TF-IDF
* Cosine Similarity

## 🧠 How It Works

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Skill Extraction
    ↓
Resume Analysis
    ↓
Skill Matching
    ↓
Resume Score
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Job Ranking
    ↓
Recommended Jobs
```

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── resume_scorer.py
├── job_recommender.py
├── requirements.txt
│
└── data/
    └── jobs.csv
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Sairam429/AI-Resume-Analyzer.git
```

Go to the project directory:

```bash
cd AI-Resume-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

## 🎯 Job Recommendation

The application compares the resume with available job descriptions using **TF-IDF and Cosine Similarity** and ranks the most relevant jobs.

## 🔮 Future Improvements

* Advanced NLP-based resume parsing
* ATS score calculation
* Resume improvement suggestions
* Education and experience extraction
* Real-time job data integration
* AI-generated resume feedback
* User authentication
* Database integration

## 👨‍💻 Author

**Sairam Yerramsetty**

GitHub: https://github.com/Sairam429
