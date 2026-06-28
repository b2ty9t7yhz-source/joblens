from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.services.job_analyzer import analyze_job_description

router = APIRouter(
    prefix="/imports",
    tags=["imports"],
)


@router.post(
    "/from-description",
    response_model=schemas.ImportedApplicationResponse,
    status_code=201,
)
def import_application_from_description(
    payload: schemas.ImportFromDescriptionRequest,
    db: Session = Depends(get_db),
):
    analysis = analyze_job_description(
        description=payload.description,
        user_skills=payload.user_skills,
    )

    analysis_notes = (
        f"Job Analysis Summary\n"
        f"- Match score: {analysis['match_score']}%\n"
        f"- Role level: {analysis['role_level']}\n"
        f"- Job family: {analysis['job_family']}\n"
        f"- Location type: {analysis['location_type']}\n"
        f"- Matched skills: {', '.join(analysis['matched_skills']) or 'None'}\n"
        f"- Missing skills: {', '.join(analysis['missing_skills']) or 'None'}\n"
        f"- Recommendation: {analysis['recommendation']}\n"
    )

    if payload.notes:
        combined_notes = f"{payload.notes}\n\n{analysis_notes}"
    else:
        combined_notes = analysis_notes

    application_data = schemas.ApplicationCreate(
        company=payload.company,
        role=payload.role,
        link=payload.link,
        type=payload.type or analysis["job_family"],
        location=payload.location or analysis["location_type"],
        source=payload.source,
        status=payload.status,
        deadline=payload.deadline,
        date_applied=payload.date_applied,
        resume_version=payload.resume_version,
        notes=combined_notes,
    )

    application = crud.create_application(
        db=db,
        application=application_data,
    )

    return {
        "application": application,
        "analysis": analysis,
    }
