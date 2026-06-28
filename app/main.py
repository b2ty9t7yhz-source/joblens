from fastapi import FastAPI

app = FastAPI(
    title="Internship Application Intelligence Tracker",
    description="A backend API for tracking internship applications, deadlines, resume versions, follow-ups, and application statistics.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {
        "message": "Internship Application Intelligence Tracker API",
        "status": "planning"
    }
