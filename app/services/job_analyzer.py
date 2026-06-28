from typing import Dict, List, Set


SKILL_KEYWORDS: Dict[str, List[str]] = {
    "Python": ["python"],
    "Java": ["java"],
    "JavaScript": ["javascript", "typescript", "node.js", "node"],
    "SQL": ["sql", "postgresql", "mysql", "sqlite", "database"],
    "FastAPI": ["fastapi"],
    "Django": ["django"],
    "Flask": ["flask"],
    "REST API": ["rest api", "restful", "api endpoint", "apis"],
    "Git": ["git", "github", "version control"],
    "Docker": ["docker", "container", "containers"],
    "AWS": ["aws", "amazon web services", "cloud"],
    "React": ["react", "react.js"],
    "HTML/CSS": ["html", "css", "tailwind"],
    "Linux": ["linux", "unix", "bash", "shell"],
    "CI/CD": ["ci/cd", "github actions", "continuous integration"],
    "Pandas": ["pandas"],
    "Machine Learning": ["machine learning", "ml", "scikit-learn", "tensorflow", "pytorch"],
    "Data Structures": ["data structures", "algorithms"],
    "Testing": ["testing", "pytest", "unit test", "integration test"],
}


def detect_skills(description: str) -> List[str]:
    text = description.lower()
    detected: List[str] = []

    for skill, keywords in SKILL_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            detected.append(skill)

    return detected


def normalize_user_skills(user_skills: List[str]) -> Set[str]:
    normalized: Set[str] = set()

    for user_skill in user_skills:
        user_skill_lower = user_skill.lower().strip()

        for canonical_skill, keywords in SKILL_KEYWORDS.items():
            all_names = [canonical_skill.lower()] + keywords
            if user_skill_lower in all_names:
                normalized.add(canonical_skill)

    return normalized


def detect_role_level(description: str) -> str:
    text = description.lower()

    if any(word in text for word in ["intern", "internship", "co-op", "coop"]):
        return "Internship"

    if any(word in text for word in ["new grad", "entry level", "junior", "early career"]):
        return "Entry Level"

    if any(word in text for word in ["senior", "staff", "principal", "lead"]):
        return "Senior"

    return "Unclear"


def detect_job_family(description: str) -> str:
    text = description.lower()

    if any(word in text for word in ["data analyst", "data engineer", "analytics", "business intelligence"]):
        return "Data"

    if any(word in text for word in ["backend", "back-end", "api", "server", "database"]):
        return "Backend"

    if any(word in text for word in ["frontend", "front-end", "react", "web developer", "full stack", "full-stack"]):
        return "Web / Full Stack"

    if any(word in text for word in ["machine learning", "ml", "ai", "artificial intelligence"]):
        return "AI / ML"

    if any(word in text for word in ["qa", "quality assurance", "test automation", "automation testing"]):
        return "QA / Automation"

    if any(word in text for word in ["it support", "help desk", "technical support", "systems"]):
        return "IT / Support"

    return "Software Engineering"


def detect_location_type(description: str) -> str:
    text = description.lower()

    if "remote" in text:
        return "Remote"

    if "hybrid" in text:
        return "Hybrid"

    if any(word in text for word in ["on-site", "onsite", "in office", "in-person"]):
        return "On-site"

    return "Unclear"


def make_recommendation(match_score: int) -> str:
    if match_score >= 80:
        return "Strong match - apply soon"

    if match_score >= 60:
        return "Good match - worth applying"

    if match_score >= 40:
        return "Stretch role - apply if interested"

    return "Low match - save as backup or learn missing skills"


def analyze_job_description(description: str, user_skills: List[str]) -> dict:
    detected_skills = detect_skills(description)
    normalized_user_skills = normalize_user_skills(user_skills)

    matched_skills = [
        skill for skill in detected_skills
        if skill in normalized_user_skills
    ]

    missing_skills = [
        skill for skill in detected_skills
        if skill not in normalized_user_skills
    ]

    if detected_skills:
        match_score = round(len(matched_skills) / len(detected_skills) * 100)
    else:
        match_score = 0

    return {
        "detected_skills": detected_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": match_score,
        "role_level": detect_role_level(description),
        "job_family": detect_job_family(description),
        "location_type": detect_location_type(description),
        "recommendation": make_recommendation(match_score),
    }
