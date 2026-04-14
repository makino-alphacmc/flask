"""empty message

Revision ID: c538b78b21f6
Revises: 9f4b0d4c8e2a
Create Date: 2026-04-14 16:56:28.879226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c538b78b21f6'
down_revision = '9f4b0d4c8e2a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('summary', sa.String(length=140), nullable=True),
    sa.Column('featured_image', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('blog_post')
