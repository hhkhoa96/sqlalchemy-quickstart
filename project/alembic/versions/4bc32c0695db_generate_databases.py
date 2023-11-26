"""Generate databases

Revision ID: 4bc32c0695db
Revises: b340b0cc05e8
Create Date: 2023-11-26 08:09:23.552097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4bc32c0695db'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "company",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(256), nullable=True),
        sa.Column("description", sa.String(256),),
        sa.Column("mode", sa.Integer),
        sa.Column("rating", sa.Float, nullable=False),
    )
    
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("username", sa.String, nullable=False),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("is_active", sa.Boolean, default=False),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column("company_id", sa.Integer, nullable=False),
    )
    
    op.create_table(
        "task",
        sa.Column("id", sa.Integer,  primary_key=True),
        sa.Column("summary", sa.String),
        sa.Column("description", sa.String),
        sa.Column("status", sa.String),
        sa.Column("priority", sa.String),
        sa.Column("user_id", sa.Integer, nullable=False),
    )
    
    op.create_foreign_key("fk_company_user", "user", "company", ["company_id"], ["id"])
    op.create_foreign_key("fk_user_task", "task", "user", ["user_id"], ["id"])


def downgrade() -> None:
    op.drop_table("company")
    op.drop_table("user")
    op.drop_table("task")

