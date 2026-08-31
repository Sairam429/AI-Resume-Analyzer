
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_jobs(resume_text, jobs, top_n=5):

    # Combine job skills and job description
    jobs["combined_text"] = (
        jobs["skills"].fillna("")
        + " "
        + jobs["job_description"].fillna("")
    )

    # Create TF-IDF vectors
    documents = [resume_text] + jobs["combined_text"].tolist()

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    # Compare resume with every job
    resume_vector = tfidf_matrix[0]
    job_vectors = tfidf_matrix[1:]

    similarities = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]

    # Add similarity score
    jobs = jobs.copy()

    jobs["match_score"] = (
        similarities * 100
    ).round(2)

    # Sort highest score first
    recommendations = jobs.sort_values(
        by="match_score",
        ascending=False
    )

    return recommendations.head(top_n)

