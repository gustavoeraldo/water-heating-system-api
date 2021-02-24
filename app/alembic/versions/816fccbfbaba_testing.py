"""testing

trying to link measurements and measures_type tables

Revision ID: 816fccbfbaba
Revises: ac7980e4f3f1
Create Date: 2021-02-24 10:30:09.899399

"""
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '816fccbfbaba'
down_revision = 'ac7980e4f3f1'
branch_labels = None
depends_on = None


def upgrade():
  op.create_table('measures_type', 
  sa.Column('id', Integer(), autoincrement=True, index=True),
  sa.Column('name', sa.String(), nullable=False),
  sa.PrimaryKeyConstraint('id')
  )
  op.create_index(op.f('ix_measures_type'), 'measures_type', ['id'], unique=False)

  op.create_table('measurements',
  sa.Column('id', sa.Integer, autoincrement=True, nullable=False, index=True),
  sa.Column('value', sa.Float, nullable=False, index=True),
  sa.Column('tag', sa.String(20), index=True),
  sa.Column('type_id', sa.Integer, nullable=False, index=True),
  sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
  sa.Column('updated_at', sa.DateTime(now), nullable=True),
  sa.Column('deleted_at', sa.DateTime(now), nullable=True),
  sa.ForeignKeyConstraint(['type_id'], ['measures_type.id']),
  sa.PrimaryKeyConstraint('id')
  )
  op.create_index(op.f('ix_measurements'), 'measurements', ['id'], unique=False)
  

def downgrade():
  op.drop_table('measurements'),
  op.drop_table('measures_type'),
