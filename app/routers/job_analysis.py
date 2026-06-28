from fastapi import APIRouter

from app import schemas
from app.services.job_analyzer import analyze_job_description

router = APIRouter(
    prefix="/jobs",
    tags=["job analysis"],
)


@router.post(
    "/analyze-description",
    response_model=schemas.JobDescriptionAnalysisResponse,
)
def analyze_description(payload: schemas.JobDescriptionAnalysisRequest):
    return analyze_job_description(
        description=payload.description,
        user_skills=payload.user_skills,
    )
