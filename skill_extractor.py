
import re

SKILLS = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "SQL",
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Django",
    "Flask",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Natural Language Processing",
    "Data Science",
    "Data Analysis",
    "Power BI",
    "Tableau",
    "Excel",
    "AWS",
    "Azure",
    "Docker",
    "Git",
    "GitHub",
    "Hadoop",
    "Spark",
    "Statistics",
]


def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills
