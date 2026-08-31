def calculate_resume_score(resume_skills, required_skills):

    if not required_skills:
        return 0

    resume_skills = set(
        skill.lower() for skill in resume_skills
    )

    required_skills = set(
        skill.lower() for skill in required_skills
    )

    matched_skills = resume_skills.intersection(required_skills)

    score = (len(matched_skills) / len(required_skills)) * 100

    return round(score, 2)


def get_missing_skills(resume_skills, required_skills):

    resume_skills = set(
        skill.lower() for skill in resume_skills
    )

    required_skills = set(
        skill.lower() for skill in required_skills
    )

    missing = required_skills - resume_skills

    return sorted(missing)