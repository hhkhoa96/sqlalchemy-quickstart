"""Generate company table

Revision ID: b340b0cc05e8
Revises: 1d7255523876
Create Date: 2023-11-26 07:47:31.622915

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b340b0cc05e8'
down_revision: Union[str, None] = '1d7255523876'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "companies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(256), nullable=True),
        sa.Column("description", sa.String(256),),
        sa.Column("mode", sa.Integer, primary_key=True),
        sa.Column("rating", sa.Float, nullable=False) 
    )


def downgrade() -> None:
    pass
