from datetime import date, timedelta
from typing import Dict, List

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models import Application


def count_applications_by_status(db: Session) -> Dict[str, int]:
    rows = (
        db.query(Application.status, func.count(Application.id))
        .group_by(Application.status)
        .all()
    )

    return {status: count for status, count in rows}


def count_applications_by_source(db: Session) -> Dict[str, int]:
    rows = (
        db.query(Application.source, func.count(Application.id))
        .group_by(Application.source)
        .all()
    )

    result = {}

    for source, count in rows:
        key = source or "Unknown"
        result[key] = count

    return result


def get_application_summary(db: Session) -> dict:
    total = db.query(Application).count()

    by_status = count_applications_by_status(db)

    upcoming_count = (
        db.query(Application)
        .filter(Application.deadline.isnot(None))
        .filter(Application.deadline >= date.today())
        .filter(Application.deadline <= date.today() + timedelta(days=14))
        .filter(~Application.status.in_(["Rejected", "Offer"]))
        .count()
    )

    return {
        "total_applications": total,
        "saved": by_status.get("Saved", 0),
        "applied": by_status.get("Applied", 0),
        "oa": by_status.get("OA", 0),
        "interview": by_status.get("Interview", 0),
        "rejected": by_status.get("Rejected", 0),
        "offer": by_status.get("Offer", 0),
        "no_response": by_status.get("No Response", 0),
        "upcoming_deadlines_next_14_days": upcoming_count,
    }


def get_upcoming_deadlines(db: Session, days: int = 14) -> List[dict]:
    today = date.today()
    end_date = today + timedelta(days=days)

    applications = (
        db.query(Application)
        .filter(Application.deadline.isnot(None))
        .filter(Application.deadline >= today)
        .filter(Application.deadline <= end_date)
        .filter(~Application.status.in_(["Rejected", "Offer"]))
        .order_by(Application.deadline.asc())
        .all()
    )

    results = []

    for application in applications:
        results.append(
            {
                "id": application.id,
                "company": application.company,
                "role": application.role,
                "status": application.status,
                "deadline": application.deadline,
                "days_left": (application.deadline - today).days,
                "source": application.source,
                "link": application.link,
            }
        )

    return results
