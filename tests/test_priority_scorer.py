from datetime import date, timedelta

from fastapi.testclient import TestClient

from app.main import app
from app.services.priority_scorer import score_job_priority

client = TestClient(app)


def test_score_job_priority_service_high_match():
    result = score_job_priority(
        match_score=80,
        role_level="Internship",
        location_type="Remote",
        deadline=date.today() + timedelta(days=5),
        preferred_locations=["Remote"],
        missing_skills=["AWS"],
    )

    assert result["priority_score"] >= 70
    assert result["priority_level"] in ["Medium", "High"]
    assert "Apply" in result["recommendation"] or "Worth" in result["recommendation"]


def test_score_priority_endpoint():
    response = client.post(
        "/jobs/score-priority",
        json={
            "description": "We are hiring a remote Software Engineer Intern with Python, SQL, REST API, Git, Docker, and AWS experience.",
            "user_skills": ["Python", "SQL", "REST API", "Git"],
            "deadline": (date.today() + timedelta(days=7)).isoformat(),
            "preferred_locations": ["Remote"],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["priority_score"] > 0
    assert data["priority_level"] in ["High", "Medium", "Low", "Very Low"]
    assert "analysis" in data
    assert data["analysis"]["role_level"] == "Internship"
    assert data["analysis"]["location_type"] == "Remote"
    assert "AWS" in data["analysis"]["missing_skills"]
