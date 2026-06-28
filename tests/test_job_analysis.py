from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_analyze_job_description():
    response = client.post(
        "/jobs/analyze-description",
        json={
            "description": "We are looking for a Software Engineer Intern with Python, SQL, REST API, Git, and AWS experience. This is a remote internship.",
            "user_skills": ["Python", "SQL", "REST API", "Git"],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["role_level"] == "Internship"
    assert data["location_type"] == "Remote"
    assert "Python" in data["detected_skills"]
    assert "SQL" in data["detected_skills"]
    assert "AWS" in data["missing_skills"]
    assert data["match_score"] > 0
