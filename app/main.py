from fastapi import FastAPI

from app.database import Base, engine
from app.routers import applications, job_analysis

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Internship Application Intelligence Tracker",
    description="A backend API for tracking internship applications, deadlines, resume versions, follow-ups, and application statistics.",
    version="0.1.0",
)

app.include_router(applications.router)
app.include_router(job_analysis.router)

@app.get("/")
def read_root():
    return {
        "message": "Internship Application Intelligence Tracker API",
        "status": "V1 CRUD in progress"
    }
