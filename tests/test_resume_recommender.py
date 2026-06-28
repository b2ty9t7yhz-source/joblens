from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_resume_recommendation_endpoint():
    response = client.post(
        "/resumes/recommend",
        json={
            "description": "We are hiring a backend Software Engineer Intern with Python, SQL, REST API, FastAPI, Docker, and AWS experience.",
            "resume_versions": [
                {
                    "name": "resume_general_swe_v1",
                    "focus_area": "General SWE",
                    "skills": ["Python", "Java", "Git", "Data Structures"],
                },
                {
                    "name": "resume_backend_v1",
                    "focus_area": "Backend",
                    "skills": ["Python", "SQL", "REST API", "FastAPI", "Git", "Docker"],
                },
                {
                    "name": "resume_data_v1",
                    "focus_area": "Data",
                    "skills": ["Python", "SQL", "Pandas", "Machine Learning"],
                },
            ],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["recommended_resume"]["name"] == "resume_backend_v1"
    assert data["recommended_resume"]["score"] > 0
    assert "Python" in data["recommended_resume"]["matched_skills"]
    assert "job_analysis" in data
    assert data["job_analysis"]["job_family"] == "Backend"
