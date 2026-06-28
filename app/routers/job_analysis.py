from fastapi import APIRouter

from app import schemas
from app.services.job_analyzer import analyze_job_description
from app.services.priority_scorer import score_job_priority

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


@router.post(
    "/score-priority",
    response_model=schemas.JobPriorityScoreResponse,
)
def score_priority(payload: schemas.JobPriorityScoreRequest):
    analysis = analyze_job_description(
        description=payload.description,
        user_skills=payload.user_skills,
    )

    priority = score_job_priority(
        match_score=analysis["match_score"],
        role_level=analysis["role_level"],
        location_type=analysis["location_type"],
        deadline=payload.deadline,
        preferred_locations=payload.preferred_locations,
        missing_skills=analysis["missing_skills"],
    )

    return {
        **priority,
        "analysis": analysis,
    }

