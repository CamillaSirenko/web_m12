"""Init

Revision ID: 1af3d5b4e770
Revises: 
Create Date: 2023-12-13 09:52:57.479456

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1af3d5b4e770'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'contacts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('phone_number', sa.String, nullable=False),
        sa.Column('birthday', sa.DateTime, nullable=False),
        sa.Column('additional_data', sa.String),
    )


def downgrade() -> None:
    op.drop_table('contacts')

