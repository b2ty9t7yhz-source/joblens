# Database Schema Draft

## V1 Table: applications

Fields:
- id
- company
- role
- link
- type
- location
- source
- status
- deadline
- date_applied
- resume_version
- notes
- created_at
- updated_at

## Future Table: users

Fields:
- id
- email
- hashed_password
- created_at

## Future Table: interviews

Fields:
- id
- application_id
- interview_type
- interview_date
- notes
- result
- created_at

## Future Table: follow_ups

Fields:
- id
- application_id
- follow_up_date
- message
- completed
- created_at

## Future Table: resume_versions

Fields:
- id
- user_id
- name
- file_link
- notes
- created_at
