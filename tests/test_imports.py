from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_import_application_from_description():
    response = client.post(
        "/imports/from-description",
        json={
            "company": "Demo Company",
            "role": "Backend Engineer Intern",
            "description": "We are hiring a remote backend intern with Python, SQL, REST API, Git, Docker, and AWS experience.",
            "link": "https://example.com/demo-job",
            "source": "Manual Import",
            "resume_version": "resume_v0",
            "user_skills": ["Python", "SQL", "REST API", "Git"],
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["application"]["company"] == "Demo Company"
    assert data["application"]["role"] == "Backend Engineer Intern"
    assert data["application"]["status"] == "Saved"
    assert "Job Analysis Summary" in data["application"]["notes"]
    assert data["analysis"]["role_level"] == "Internship"
    assert data["analysis"]["location_type"] == "Remote"
    assert "AWS" in data["analysis"]["missing_skills"]
