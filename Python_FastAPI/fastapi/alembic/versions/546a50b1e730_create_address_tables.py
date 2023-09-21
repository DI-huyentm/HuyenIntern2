"""Create address tables

Revision ID: 546a50b1e730
Revises: 82c41b89a4d7
Create Date: 2023-09-06 15:06:03.659231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '546a50b1e730'
down_revision: Union[str, None] = '82c41b89a4d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(200), nullable=False),
                    sa.Column('address2', sa.String(200), nullable=False),
                    sa.Column('city', sa.String(200), nullable=False),
                    sa.Column('state', sa.String(200), nullable=False),
                    sa.Column('country', sa.String(200), nullable=False),
                    sa.Column('postalcode', sa.String(200), nullable=False),
                    )


def downgrade() -> None:
    op.drop_column('address')
