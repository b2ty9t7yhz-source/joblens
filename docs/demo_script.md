# Demo Script

This document explains how to demo the JobLens.

## 1. Start the app

Run:

    source .venv/bin/activate
    python -m uvicorn app.main:app --reload

Open the web UI:

    http://127.0.0.1:8000/ui

Open the API docs:

    http://127.0.0.1:8000/docs

## 2. Show the dashboard

Explain:
- The dashboard summarizes saved applications.
- It tracks total applications, saved roles, applied roles, interviews, and upcoming deadlines.

## 3. Add an application manually

Example:
- Company: Demo Company
- Role: Backend Engineer Intern
- Location: Remote
- Source: Manual
- Status: Saved
- Resume Version: resume_v0

Explain:
- This uses the FastAPI backend.
- The data is saved in SQLite through SQLAlchemy.

## 4. Analyze a job description

Use this job description:

    We are hiring a remote backend Software Engineer Intern with Python, SQL, REST API, FastAPI, Docker, and AWS experience.

Use these skills:

    Python, SQL, REST API, FastAPI, Git

Explain:
- The app detects required skills.
- It compares them with the user's skills.
- It returns matched skills, missing skills, job family, role level, and match score.

## 5. Import from job description

Use the same job description.

Explain:
- The app analyzes the job description.
- It generates an analysis summary.
- It saves the role as an application automatically.

## 6. Generate intelligence report

Explain:
- This combines skill analysis, priority scoring, resume recommendation, and action items.
- The goal is to help students decide which roles to apply to first.

## 7. Show API docs

Open:

    http://127.0.0.1:8000/docs

Point out:
- Applications CRUD API
- Job description analyzer
- Import workflow
- Stats endpoints
- Resume recommendation
- Intelligence report
