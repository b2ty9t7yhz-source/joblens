from typing import Any, Dict, List, Optional

import httpx

from app.services.job_analyzer import analyze_job_description


GREENHOUSE_API_BASE_URL = "https://boards-api.greenhouse.io/v1/boards"


def fetch_greenhouse_jobs(board_token: str) -> List[Dict[str, Any]]:
    url = f"{GREENHOUSE_API_BASE_URL}/{board_token}/jobs"

    response = httpx.get(
        url,
        params={"content": "true"},
        timeout=15,
    )

    response.raise_for_status()

    data = response.json()
    return data.get("jobs", [])


def clean_html_content(content: Optional[str]) -> str:
    if not content:
        return ""

    text = content

    replacements = {
        "<br>": "\n",
        "<br/>": "\n",
        "<br />": "\n",
        "</p>": "\n",
        "</li>": "\n",
        "<li>": "- ",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    import re

    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def job_matches_keywords(
    job: Dict[str, Any],
    keywords: Optional[List[str]],
) -> bool:
    if not keywords:
        return True

    title = job.get("title", "") or ""
    content = clean_html_content(job.get("content", ""))

    searchable_text = f"{title} {content}".lower()

    return any(keyword.lower() in searchable_text for keyword in keywords)


def job_matches_location(
    job: Dict[str, Any],
    locations: Optional[List[str]],
) -> bool:
    if not locations:
        return True

    location_data = job.get("location") or {}
    location_name = location_data.get("name", "") or ""

    searchable_location = location_name.lower()

    return any(location.lower() in searchable_location for location in locations)


def normalize_greenhouse_job(
    job: Dict[str, Any],
    company: str,
    source: str = "Greenhouse",
) -> Dict[str, Any]:
    description = clean_html_content(job.get("content", ""))

    location_data = job.get("location") or {}
    location_name = location_data.get("name", "")

    absolute_url = job.get("absolute_url")

    return {
        "company": company,
        "role": job.get("title", "Unknown Role"),
        "link": absolute_url,
        "location": location_name,
        "source": source,
        "description": description,
        "greenhouse_job_id": job.get("id"),
    }


def import_greenhouse_jobs_preview(
    board_token: str,
    company: str,
    keywords: Optional[List[str]] = None,
    locations: Optional[List[str]] = None,
    user_skills: Optional[List[str]] = None,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    raw_jobs = fetch_greenhouse_jobs(board_token=board_token)

    imported_jobs: List[Dict[str, Any]] = []

    for job in raw_jobs:
        if not job_matches_keywords(job, keywords):
            continue

        if not job_matches_location(job, locations):
            continue

        normalized_job = normalize_greenhouse_job(
            job=job,
            company=company,
        )

        analysis = analyze_job_description(
            description=normalized_job["description"],
            user_skills=user_skills or [],
        )

        imported_jobs.append(
            {
                "job": normalized_job,
                "analysis": analysis,
            }
        )

        if len(imported_jobs) >= limit:
            break

    return imported_jobs
