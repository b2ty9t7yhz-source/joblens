from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_db
from app.services.demo_data import (
    clear_sample_data,
    get_demo_applications,
    load_sample_data,
)


router = APIRouter(prefix="/demo", tags=["demo"])


@router.get("/status", response_model=schemas.DemoStatusResponse)
def read_demo_status(db: Session = Depends(get_db)):
    applications = get_demo_applications(db)
    return {
        "active": bool(applications),
        "sample_records": len(applications),
    }


@router.post("/load-sample-data", response_model=schemas.DemoLoadResponse)
def load_demo_sample_data(db: Session = Depends(get_db)):
    inserted, skipped, applications = load_sample_data(db)
    return {
        "inserted": inserted,
        "skipped": skipped,
        "total_sample_records": len(applications),
        "applications": applications,
    }


@router.delete("/sample-data", response_model=schemas.DemoClearResponse)
def clear_demo_sample_data(db: Session = Depends(get_db)):
    return {"deleted": clear_sample_data(db)}
