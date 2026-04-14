"""empty message

Revision ID: f3a696091dee
Revises: 
Create Date: 2026-04-14 14:59:17.901058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3a696091dee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # This database already had the base users table when migrations were initialized.
    # Keep the first revision as a no-op baseline and apply later schema changes in
    # subsequent revisions.
    pass


def downgrade():
    pass
