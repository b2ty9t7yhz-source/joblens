from fastapi import APIRouter

from app import schemas
from app.services.resume_recommender import recommend_resume_version

router = APIRouter(
    prefix="/resumes",
    tags=["resumes"],
)


@router.post(
    "/recommend",
    response_model=schemas.ResumeRecommendationResponse,
)
def recommend_resume(payload: schemas.ResumeRecommendationRequest):
    resume_versions = [
        resume.model_dump()
        for resume in payload.resume_versions
    ]

    return recommend_resume_version(
        description=payload.description,
        resume_versions=resume_versions,
    )
