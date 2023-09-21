"""Create apt_num for address

Revision ID: 17c3fffaf806
Revises: 49a6599f639c
Create Date: 2023-09-07 10:13:28.662046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17c3fffaf806'
down_revision: Union[str, None] = '49a6599f639c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('address', sa.Column('apt_num', sa.String(10), nullable=True))

def downgrade() -> None:
    op.drop_column('address', 'apt_num')
