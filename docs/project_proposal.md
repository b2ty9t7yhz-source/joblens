# JobLens

## Problem

Students applying to internships, new grad roles, research assistant roles, and technical part-time jobs often lose track of applications, deadlines, resume versions, interview stages, follow-up dates, and company-specific notes.

A simple spreadsheet works at first, but it becomes harder to manage as the number of applications grows.

## Target Users

College students applying for:
- Software engineering internships
- New grad software roles
- Research assistant positions
- Technical part-time jobs
- Data, QA, IT, and automation internships

## Core Idea

Build a backend system that helps students track the entire job application pipeline.

The project will start as a FastAPI CRUD API and gradually become a more professional backend system with authentication, testing, migrations, statistics, reminders, and deployment.

## Engineering Goals

This project is designed to go beyond a basic CRUD application.

The goal is to build a backend system with:
- Clean API design
- Relational database modeling
- Authentication
- Automated testing
- Database migrations
- Filtering and pagination
- Analytics endpoints
- Follow-up reminders
- Future deployment

## Version Plan

### V1: Core Application Tracking
- Add, view, update, and delete job applications
- Track company, role, link, source, status, deadline, notes, and resume version
- Search by company
- Filter by status
- Track application deadline
- Track date applied

### V2: Engineering Quality
- Add pytest tests
- Add Alembic database migrations
- Add pagination and sorting
- Improve error handling
- Document API endpoints
- Add status enum validation

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

## Why This Project Is Strong

This project is stronger than a basic todo list or simple CRUD app because it connects directly to a real problem: managing internship applications.

It also gives me a way to practice backend engineering concepts that appear in real software systems, including database modeling, API design, authentication, testing, migrations, analytics, and automation.
