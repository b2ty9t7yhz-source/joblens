from typing import Optional

from sqlalchemy.orm import Session

from app import models, schemas

def create_application(db: Session, application: schemas.ApplicationCreate):
    db_application = models.Application(**application.model_dump())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

def get_application(db: Session, application_id: int):
    return (
        db.query(models.Application)
        .filter(models.Application.id == application_id)
        .first()
    )

def get_applications(
    db: Session,
    company: Optional[str] = None,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
):
    query = db.query(models.Application)

    if company:
        query = query.filter(models.Application.company.ilike(f"%{company}%"))

    if status:
        query = query.filter(models.Application.status == status)

    return (
        query
        .order_by(models.Application.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def update_application(
    db: Session,
    db_application: models.Application,
    updates: schemas.ApplicationUpdate,
):
    update_data = updates.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_application, field, value)

    db.commit()
    db.refresh(db_application)
    return db_application

def delete_application(db: Session, db_application: models.Application):
    db.delete(db_application)
    db.commit()
    return db_application
