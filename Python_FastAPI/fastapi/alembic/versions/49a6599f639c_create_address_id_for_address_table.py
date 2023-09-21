"""Create address_id for users

Revision ID: 49a6599f639c
Revises: 546a50b1e730
Create Date: 2023-09-06 15:20:57.107861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49a6599f639c'
down_revision: Union[str, None] = '546a50b1e730'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk',
                          source_table="users", referent_table="address",
                          local_cols=['address_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name='users')
    op.drop_column('users', 'address_id')

