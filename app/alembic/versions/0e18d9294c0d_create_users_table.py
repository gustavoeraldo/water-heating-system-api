"""create users table

Revision ID: 0e18d9294c0d
Revises: 
Create Date: 2021-02-14 19:58:25.335646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e18d9294c0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('temp_table',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('username', sa.String(20), nullable=True),
    sa.Column('active', sa.Boolean, nullable=True)
    )


def downgrade():
  op.drop_table('temp_table')
