from datetime import date
from typing import List, Optional


def calculate_deadline_bonus(deadline: Optional[date]) -> tuple[int, str | None]:
    if deadline is None:
        return 0, None

    days_left = (deadline - date.today()).days

    if days_left < 0:
        return -30, "Deadline has already passed"

    if days_left <= 3:
        return 15, "Deadline is within 3 days"

    if days_left <= 7:
        return 10, "Deadline is within 7 days"

    if days_left <= 14:
        return 5, "Deadline is within 14 days"

    return 0, None


def calculate_role_level_bonus(role_level: str) -> tuple[int, str | None]:
    if role_level == "Internship":
        return 15, "Internship-level role"

    if role_level == "Entry Level":
        return 10, "Entry-level role"

    if role_level == "Senior":
        return -25, "Role appears senior-level"

    return 0, None


def calculate_location_bonus(
    location_type: str,
    preferred_locations: List[str],
) -> tuple[int, str | None]:
    normalized_preferences = {
        location.lower().strip()
        for location in preferred_locations
    }

    location_lower = location_type.lower()

    if not normalized_preferences:
        return 0, None

    if location_lower in normalized_preferences:
        return 10, f"Location type matches preference: {location_type}"

    if location_lower == "remote" and "remote" in normalized_preferences:
        return 10, "Remote role matches preference"

    if location_lower == "unclear":
        return 0, None

    return -5, f"Location type may not match preference: {location_type}"


def calculate_skill_score_component(match_score: int) -> tuple[int, str]:
    if match_score >= 80:
        return 45, "Strong skill match"

    if match_score >= 60:
        return 35, "Good skill match"

    if match_score >= 40:
        return 20, "Partial skill match"

    if match_score > 0:
        return 10, "Low but nonzero skill match"

    return 0, "No detected skill match"


def get_priority_level(score: int) -> str:
    if score >= 80:
        return "High"

    if score >= 60:
        return "Medium"

    if score >= 40:
        return "Low"

    return "Very Low"


def get_priority_recommendation(score: int) -> str:
    if score >= 80:
        return "Apply soon"

    if score >= 60:
        return "Worth applying"

    if score >= 40:
        return "Save as backup or improve fit first"

    return "Low priority"


def score_job_priority(
    match_score: int,
    role_level: str,
    location_type: str,
    deadline: Optional[date] = None,
    preferred_locations: Optional[List[str]] = None,
    missing_skills: Optional[List[str]] = None,
) -> dict:
    preferred_locations = preferred_locations or []
    missing_skills = missing_skills or []

    score = 0
    reasons: List[str] = []

    skill_points, skill_reason = calculate_skill_score_component(match_score)
    score += skill_points
    reasons.append(skill_reason)

    role_points, role_reason = calculate_role_level_bonus(role_level)
    score += role_points
    if role_reason:
        reasons.append(role_reason)

    location_points, location_reason = calculate_location_bonus(
        location_type=location_type,
        preferred_locations=preferred_locations,
    )
    score += location_points
    if location_reason:
        reasons.append(location_reason)

    deadline_points, deadline_reason = calculate_deadline_bonus(deadline)
    score += deadline_points
    if deadline_reason:
        reasons.append(deadline_reason)

    if len(missing_skills) >= 5:
        score -= 10
        reasons.append("Many missing skills")

    elif len(missing_skills) >= 3:
        score -= 5
        reasons.append("Some missing skills")

    score = max(0, min(100, score))

    return {
        "priority_score": score,
        "priority_level": get_priority_level(score),
        "recommendation": get_priority_recommendation(score),
        "reasons": reasons,
    }
