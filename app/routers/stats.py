from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.analytics import (
    count_applications_by_source,
    count_applications_by_status,
    get_application_summary,
    get_upcoming_deadlines,
)

router = APIRouter(
    prefix="/stats",
    tags=["stats"],
)


@router.get("/summary")
def read_summary(db: Session = Depends(get_db)):
    return get_application_summary(db)


@router.get("/applications-by-status")
def read_applications_by_status(db: Session = Depends(get_db)):
    return count_applications_by_status(db)


@router.get("/applications-by-source")
def read_applications_by_source(db: Session = Depends(get_db)):
    return count_applications_by_source(db)


@router.get("/upcoming-deadlines")
def read_upcoming_deadlines(
    days: int = Query(default=14, ge=1, le=365),
    db: Session = Depends(get_db),
):
    return get_upcoming_deadlines(db=db, days=days)
