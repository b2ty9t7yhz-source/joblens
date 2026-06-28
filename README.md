# Internship Application Intelligence Tracker

A backend system for tracking internship and new grad job applications, resume versions, deadlines, interview stages, follow-ups, and application statistics.

## Goal

This project helps students manage the full internship application process while practicing professional backend engineering skills.

The project starts as a FastAPI CRUD API and gradually adds authentication, database migrations, testing, analytics, reminders, Docker, and deployment.

## Core Features

### V1: Core Application Tracking
- Add job applications
- View all applications
- View one application
- Update application status
- Delete applications
- Search by company
- Filter by status
- Track application deadline
- Track resume version
- Add notes

### V2: Engineering Quality
- Add pytest tests
- Add Alembic database migrations
- Add pagination and sorting
- Improve error handling
- Document API endpoints

### V3: Multi-User System
- Add user registration and login
- Add JWT authentication
- Ensure users can only access their own applications
- Add user-specific application statistics

### V4: Intelligence and Automation
- Add follow-up reminders
- Add upcoming deadline endpoint
- Add application analytics
- Add resume-to-job keyword matching
- Deploy with PostgreSQL and Docker

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- pytest
- Alembic
- JWT Authentication
- Docker
- PostgreSQL

## Planned API Endpoints

```text
GET    /applications
POST   /applications
GET    /applications/{id}
PUT    /applications/{id}
DELETE /applications/{id}

GET    /applications?company=
GET    /applications?status=
GET    /applications?sort_by=deadline

POST   /auth/register
POST   /auth/login
GET    /users/me

GET    /stats/applications-by-status
GET    /stats/applications-by-source
GET    /applications/upcoming-deadlines
```

## Project Status

Planning and design phase.

## Next Steps

- Set up FastAPI project structure
- Design SQLAlchemy models
- Create SQLite database
- Implement V1 CRUD endpoints
- Add pytest tests
- Add Alembic migrations
