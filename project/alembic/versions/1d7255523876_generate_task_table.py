"""generate task table

Revision ID: 1d7255523876
Revises: b1cbdba4da5c
Create Date: 2023-11-26 06:36:33.155801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d7255523876'
down_revision: Union[str, None] = 'b1cbdba4da5c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer,  primary_key=True),
        sa.Column("summary", sa.String),
        sa.Column("description", sa.String),
        sa.Column("status", sa.String),
        sa.Column("priority", sa.String),
    )


def downgrade() -> None:
    op.drop_table("tasks")
