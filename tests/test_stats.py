from datetime import date, timedelta
from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_stats_endpoints():
    company_name = f"Stats Demo Company {uuid4()}"

    create_response = client.post(
        "/applications/",
        json={
            "company": company_name,
            "role": "Software Engineer Intern",
            "link": "https://example.com/stats-demo",
            "type": "SWE Intern",
            "location": "Remote",
            "source": "LinkedIn",
            "status": "Applied",
            "deadline": (date.today() + timedelta(days=7)).isoformat(),
            "resume_version": "resume_v0",
            "notes": "Created for stats endpoint test.",
        },
    )

    assert create_response.status_code == 201

    status_response = client.get("/stats/applications-by-status")
    assert status_response.status_code == 200
    assert status_response.json()["Applied"] >= 1

    source_response = client.get("/stats/applications-by-source")
    assert source_response.status_code == 200
    assert source_response.json()["LinkedIn"] >= 1

    summary_response = client.get("/stats/summary")
    assert summary_response.status_code == 200
    assert summary_response.json()["total_applications"] >= 1

    deadlines_response = client.get("/stats/upcoming-deadlines?days=14")
    assert deadlines_response.status_code == 200

    upcoming = deadlines_response.json()
    assert any(item["company"] == company_name for item in upcoming)
