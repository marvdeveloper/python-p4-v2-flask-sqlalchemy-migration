"""Initial migration.

Revision ID: 4935e8a0b272
Revises: 
Create Date: 2025-06-17 10:23:32.238010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4935e8a0b272'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
