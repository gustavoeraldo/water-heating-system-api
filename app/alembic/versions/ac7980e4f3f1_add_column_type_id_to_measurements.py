"""add column type_id to measurements

Revision ID: ac7980e4f3f1
Revises: cdba1c697b57
Create Date: 2021-02-24 09:46:14.376973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac7980e4f3f1'
down_revision = 'cdba1c697b57'
branch_labels = None
depends_on = None


def upgrade():
  op.add_column('measurements', sa.Column('type_id', sa.Integer, nullable=False)),
  sa.ForeignKeyConstraint(['type_id'], ['measures_type.id']),


def downgrade():
  op.drop_column('measurements', 'type_id')
