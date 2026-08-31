# 🤖 AI Resume Analyzer & Job Recommendation System

An AI-powered web application that analyzes resumes, extracts relevant skills, evaluates resume-to-job compatibility, identifies missing skills, and recommends suitable job opportunities.

## 🚀 Features

* 📄 Upload resume in PDF format
* 🧠 Automatically extract skills from the resume
* 📊 Calculate resume/job match score
* 🥧 Display resume score using a pie chart
* ⚠️ Identify missing skills
* 🎯 Recommend relevant jobs
* 📈 Rank jobs based on resume-job similarity
* 🌐 Interactive web interface using Streamlit

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **PDFPlumber**
* **Plotly**
* **TF-IDF**
* **Cosine Similarity**
* **NLP**

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

## 📊 Resume Analysis

The system compares the skills detected in the resume with the skills required for a selected job.

For example:

```text
Required Skills:
Python
SQL
Pandas
Machine Learning
Power BI

Resume Skills:
Python
SQL
Pandas
Machine Learning

Resume Match Score:
80%

Missing Skill:
Power BI
```

## 🎯 Job Recommendation

The system compares the resume with multiple job descriptions using **TF-IDF and Cosine Similarity**.

Example:

```text
Data Scientist            91%
Machine Learning Engineer 87%
Data Analyst              82%
AI Engineer               79%
Python Developer          74%
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

Move into the project directory:

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

The application will open at:

```text
http://localhost:8501
```

## 📌 Future Improvements

* Advanced NLP-based resume parsing
* Automatic education and experience extraction
* ATS score calculation
* Resume improvement suggestions
* Skill-based learning recommendations
* Real-time job data integration
* User authentication
* Database integration
* AI-generated resume feedback

## 👨‍💻 Author

**Sairam Yerramsetty**

GitHub: https://github.com/Sairam429

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
