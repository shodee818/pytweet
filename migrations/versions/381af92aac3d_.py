"""empty message

Revision ID: 381af92aac3d
Revises: b83d35a03151
Create Date: 2020-01-23 17:21:06.723568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '381af92aac3d'
down_revision = 'b83d35a03151'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('comment', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.add_column('comment', sa.Column('user_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'user_id')
    op.drop_column('comment', 'updated_at')
    op.drop_column('comment', 'created_at')
    # ### end Alembic commands ###
