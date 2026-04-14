"""add administrator to users

Revision ID: 9f4b0d4c8e2a
Revises: f3a696091dee
Create Date: 2026-04-14 15:20:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f4b0d4c8e2a'
down_revision = 'f3a696091dee'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('administrator', sa.String(length=1), nullable=True))


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('administrator')
