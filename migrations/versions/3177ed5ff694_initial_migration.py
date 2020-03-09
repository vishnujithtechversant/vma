"""initial migration

Revision ID: 3177ed5ff694
Revises: 
Create Date: 2020-03-09 13:34:45.449568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3177ed5ff694'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
