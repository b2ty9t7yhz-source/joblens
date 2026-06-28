from typing import List

from app.services.job_analyzer import analyze_job_description, normalize_user_skills


def calculate_resume_skill_match(
    detected_job_skills: List[str],
    resume_skills: List[str],
) -> tuple[int, List[str], List[str]]:
    normalized_resume_skills = normalize_user_skills(resume_skills)

    matched_skills = [
        skill for skill in detected_job_skills
        if skill in normalized_resume_skills
    ]

    missing_skills = [
        skill for skill in detected_job_skills
        if skill not in normalized_resume_skills
    ]

    if detected_job_skills:
        score = round(len(matched_skills) / len(detected_job_skills) * 100)
    else:
        score = 0

    return score, matched_skills, missing_skills


def calculate_focus_bonus(job_family: str, focus_area: str) -> int:
    job_family_lower = job_family.lower()
    focus_area_lower = focus_area.lower()

    if job_family_lower == "backend" and "backend" in focus_area_lower:
        return 15

    if job_family_lower == "data" and "data" in focus_area_lower:
        return 15

    if job_family_lower == "ai / ml" and (
        "ai" in focus_area_lower or "ml" in focus_area_lower or "machine learning" in focus_area_lower
    ):
        return 15

    if job_family_lower == "web / full stack" and (
        "web" in focus_area_lower or "full stack" in focus_area_lower or "frontend" in focus_area_lower
    ):
        return 15

    if job_family_lower == "qa / automation" and (
        "qa" in focus_area_lower or "automation" in focus_area_lower or "testing" in focus_area_lower
    ):
        return 15

    if job_family_lower == "it / support" and (
        "it" in focus_area_lower or "support" in focus_area_lower
    ):
        return 15

    if "general" in focus_area_lower:
        return 5

    return 0


def recommend_resume_version(
    description: str,
    resume_versions: List[dict],
) -> dict:
    all_resume_skills = []

    for resume in resume_versions:
        all_resume_skills.extend(resume.get("skills", []))

    analysis = analyze_job_description(
        description=description,
        user_skills=all_resume_skills,
    )

    detected_job_skills = analysis["detected_skills"]
    job_family = analysis["job_family"]

    scored_resumes = []

    for resume in resume_versions:
        skill_score, matched_skills, missing_skills = calculate_resume_skill_match(
            detected_job_skills=detected_job_skills,
            resume_skills=resume.get("skills", []),
        )

        focus_bonus = calculate_focus_bonus(
            job_family=job_family,
            focus_area=resume.get("focus_area", ""),
        )

        final_score = min(100, skill_score + focus_bonus)

        reasons = []

        if matched_skills:
            reasons.append(f"Matches skills: {', '.join(matched_skills)}")

        if focus_bonus > 0:
            reasons.append(f"Focus area matches job family: {job_family}")

        if missing_skills:
            reasons.append(f"Missing skills: {', '.join(missing_skills)}")

        if not reasons:
            reasons.append("No strong match found")

        scored_resumes.append(
            {
                "name": resume.get("name"),
                "focus_area": resume.get("focus_area"),
                "score": final_score,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills,
                "reasons": reasons,
            }
        )

    scored_resumes.sort(key=lambda item: item["score"], reverse=True)

    if scored_resumes:
        best_resume = scored_resumes[0]
    else:
        best_resume = None

    return {
        "recommended_resume": best_resume,
        "all_resume_scores": scored_resumes,
        "job_analysis": analysis,
    }
