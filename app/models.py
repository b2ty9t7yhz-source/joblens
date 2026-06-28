from datetime import datetime
from sqlalchemy import Column, Date, DateTime, Integer, String, Text
from app.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String, nullable=False, index=True)
    role = Column(String, nullable=False)
    link = Column(String, nullable=True)

    type = Column(String, nullable=True)
    location = Column(String, nullable=True)
    source = Column(String, nullable=True)

    status = Column(String, nullable=False, default="Saved", index=True)

    deadline = Column(Date, nullable=True)
    date_applied = Column(Date, nullable=True)

    resume_version = Column(String, nullable=True)
    notes = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
