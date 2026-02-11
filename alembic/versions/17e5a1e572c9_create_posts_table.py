"""Create posts table

Revision ID: 17e5a1e572c9
Revises: eee8d5b22cb8
Create Date: 2026-02-11 07:44:35.208165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17e5a1e572c9'
down_revision: Union[str, Sequence[str], None] = 'eee8d5b22cb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
