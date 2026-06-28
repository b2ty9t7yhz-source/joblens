from datetime import date, datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

ApplicationStatus = Literal[
    "Saved",
    "Applied",
    "OA",
    "Interview",
    "Rejected",
    "Offer",
    "No Response",
]

class ApplicationBase(BaseModel):
    company: str
    role: str
    link: Optional[str] = None
    type: Optional[str] = None
    location: Optional[str] = None
    source: Optional[str] = None
    status: ApplicationStatus = "Saved"
    deadline: Optional[date] = None
    date_applied: Optional[date] = None
    resume_version: Optional[str] = None
    notes: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    link: Optional[str] = None
    type: Optional[str] = None
    location: Optional[str] = None
    source: Optional[str] = None
    status: Optional[ApplicationStatus] = None
    deadline: Optional[date] = None
    date_applied: Optional[date] = None
    resume_version: Optional[str] = None
    notes: Optional[str] = None

class ApplicationRead(ApplicationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class JobDescriptionAnalysisRequest(BaseModel):
    description: str
    user_skills: list[str] = []


class JobDescriptionAnalysisResponse(BaseModel):
    detected_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]
    match_score: int
    role_level: str
    job_family: str
    location_type: str
    recommendation: str
