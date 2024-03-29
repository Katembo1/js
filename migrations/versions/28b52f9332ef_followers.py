"""followers

Revision ID: 28b52f9332ef
Revises: da4fd680508c
Create Date: 2024-02-20 23:11:02.906306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28b52f9332ef'
down_revision = 'da4fd680508c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('followers', schema=None) as batch_op:
        batch_op.alter_column('follower_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('followed_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('followers', schema=None) as batch_op:
        batch_op.alter_column('followed_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('follower_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
