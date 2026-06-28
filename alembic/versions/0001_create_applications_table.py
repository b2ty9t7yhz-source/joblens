"""create applications table

Revision ID: 0001_create_applications_table
Revises:
Create Date: 2026-06-28
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0001_create_applications_table"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if "applications" in inspector.get_table_names():
        return

    op.create_table(
        "applications",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("company", sa.String(), nullable=False, index=True),
        sa.Column("role", sa.String(), nullable=False),
        sa.Column("link", sa.String(), nullable=True),
        sa.Column("type", sa.String(), nullable=True),
        sa.Column("location", sa.String(), nullable=True),
        sa.Column("source", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, default="Saved", index=True),
        sa.Column("deadline", sa.Date(), nullable=True),
        sa.Column("date_applied", sa.Date(), nullable=True),
        sa.Column("resume_version", sa.String(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if "applications" in inspector.get_table_names():
        op.drop_table("applications")
