from app.services.greenhouse_importer import (
    clean_html_content,
    job_matches_keywords,
    job_matches_location,
    normalize_greenhouse_job,
)


def test_clean_html_content():
    html = "<p>We need Python</p><p>Experience with SQL<br>REST APIs</p>"

    cleaned = clean_html_content(html)

    assert "Python" in cleaned
    assert "SQL" in cleaned
    assert "REST APIs" in cleaned
    assert "<p>" not in cleaned


def test_job_matches_keywords():
    job = {
        "title": "Software Engineer Intern",
        "content": "<p>Python and backend APIs</p>",
    }

    assert job_matches_keywords(job, ["intern"])
    assert job_matches_keywords(job, ["backend"])
    assert not job_matches_keywords(job, ["accounting"])


def test_job_matches_location():
    job = {
        "location": {
            "name": "Remote - United States"
        }
    }

    assert job_matches_location(job, ["remote"])
    assert job_matches_location(job, ["United States"])
    assert not job_matches_location(job, ["London"])


def test_normalize_greenhouse_job():
    job = {
        "id": 123,
        "title": "Backend Engineer Intern",
        "absolute_url": "https://example.com/job",
        "location": {
            "name": "Remote"
        },
        "content": "<p>Python, SQL, and APIs</p>",
    }

    normalized = normalize_greenhouse_job(
        job=job,
        company="Demo Company",
    )

    assert normalized["company"] == "Demo Company"
    assert normalized["role"] == "Backend Engineer Intern"
    assert normalized["location"] == "Remote"
    assert normalized["source"] == "Greenhouse"
    assert normalized["greenhouse_job_id"] == 123
    assert "Python" in normalized["description"]
