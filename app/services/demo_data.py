from datetime import date, timedelta

from sqlalchemy.orm import Session

from app import models


DEMO_SOURCE = "JobLens Demo"
DEMO_LINK_PREFIX = "https://demo.joblens.local/"


def _sample_applications(today: date) -> list[dict]:
    return [
        {
            "company": "Northstar Labs",
            "role": "Software Engineer Intern",
            "link": f"{DEMO_LINK_PREFIX}northstar-swe-intern",
            "type": "SWE Intern",
            "location": "New York, NY (Hybrid)",
            "source": DEMO_SOURCE,
            "status": "Saved",
            "deadline": today + timedelta(days=3),
            "resume_version": "resume_general_swe_v1",
            "notes": "[JobLens Demo] High-priority role; tailor project bullets before applying.",
        },
        {
            "company": "Atlas Cloud",
            "role": "Backend Engineering Intern",
            "link": f"{DEMO_LINK_PREFIX}atlas-backend-intern",
            "type": "Backend Intern",
            "location": "Remote",
            "source": DEMO_SOURCE,
            "status": "Applied",
            "deadline": today + timedelta(days=10),
            "date_applied": today - timedelta(days=4),
            "resume_version": "resume_backend_v1",
            "notes": "[JobLens Demo] Follow up next week. Stack: Python, FastAPI, PostgreSQL.",
        },
        {
            "company": "Juniper Analytics",
            "role": "Data Science Intern",
            "link": f"{DEMO_LINK_PREFIX}juniper-data-intern",
            "type": "Data Intern",
            "location": "Boston, MA",
            "source": DEMO_SOURCE,
            "status": "OA",
            "deadline": today + timedelta(days=21),
            "date_applied": today - timedelta(days=9),
            "resume_version": "resume_data_v1",
            "notes": "[JobLens Demo] Online assessment due in two days; review SQL and pandas.",
        },
        {
            "company": "Cedar Security",
            "role": "Security Engineering Intern",
            "link": f"{DEMO_LINK_PREFIX}cedar-security-intern",
            "type": "Security Intern",
            "location": "Washington, DC (Hybrid)",
            "source": DEMO_SOURCE,
            "status": "Interview",
            "date_applied": today - timedelta(days=16),
            "resume_version": "resume_general_swe_v1",
            "notes": "[JobLens Demo] Technical interview scheduled; prepare networking fundamentals.",
        },
        {
            "company": "Lumen Health",
            "role": "Full Stack Developer Intern",
            "link": f"{DEMO_LINK_PREFIX}lumen-fullstack-intern",
            "type": "Full Stack Intern",
            "location": "Philadelphia, PA",
            "source": DEMO_SOURCE,
            "status": "Offer",
            "date_applied": today - timedelta(days=28),
            "resume_version": "resume_general_swe_v1",
            "notes": "[JobLens Demo] Offer received; response requested by Friday.",
        },
        {
            "company": "Orbit Robotics",
            "role": "Robotics Software Intern",
            "link": f"{DEMO_LINK_PREFIX}orbit-robotics-intern",
            "type": "Robotics Intern",
            "location": "Pittsburgh, PA",
            "source": DEMO_SOURCE,
            "status": "No Response",
            "date_applied": today - timedelta(days=24),
            "resume_version": "resume_general_swe_v1",
            "notes": "[JobLens Demo] No response after three weeks; send a final follow-up.",
        },
    ]


def demo_links(today: date | None = None) -> set[str]:
    return {item["link"] for item in _sample_applications(today or date.today())}


def get_demo_applications(db: Session) -> list[models.Application]:
    return (
        db.query(models.Application)
        .filter(models.Application.link.in_(demo_links()))
        .order_by(models.Application.created_at.desc())
        .all()
    )


def load_sample_data(db: Session) -> tuple[int, int, list[models.Application]]:
    samples = _sample_applications(date.today())
    existing_links = {
        link
        for (link,) in db.query(models.Application.link)
        .filter(models.Application.link.in_([item["link"] for item in samples]))
        .all()
    }

    new_applications = [
        models.Application(**sample)
        for sample in samples
        if sample["link"] not in existing_links
    ]
    db.add_all(new_applications)
    db.commit()

    return len(new_applications), len(existing_links), get_demo_applications(db)


def clear_sample_data(db: Session) -> int:
    applications = get_demo_applications(db)
    for application in applications:
        db.delete(application)
    db.commit()
    return len(applications)
