"""add columns to measures_t

Revision ID: cdba1c697b57
Revises: 0e18d9294c0d
Create Date: 2021-02-21 13:50:06.263811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdba1c697b57'
down_revision = '0e18d9294c0d'
branch_labels = None
depends_on = None


def upgrade():
  op.add_column('measurements', sa.Column('tag', sa.String())),
  op.add_column('measurements', sa.Column('type_id', sa.Integer, nullable=False)),
  sa.ForeignKeyConstraint(['type_id'], ['measures_type.id']),

def downgrade():
  op.drop_column('measurements', 'tag'),
  op.drop_column('measurements', 'type_id'),
