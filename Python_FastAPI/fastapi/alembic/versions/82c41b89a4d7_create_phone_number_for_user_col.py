"""create phone number for user col

Revision ID: 82c41b89a4d7
Revises: 
Create Date: 2023-09-06 14:39:12.757454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82c41b89a4d7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(20), nullable=True))

def downgrade() -> None:
    op.drop_column('users', 'phone_number')
