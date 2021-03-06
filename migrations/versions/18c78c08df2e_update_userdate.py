"""update userdate

Revision ID: 18c78c08df2e
Revises: 9fe9c2bdc4e6
Create Date: 2017-11-20 16:41:27.983052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18c78c08df2e'
down_revision = '9fe9c2bdc4e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('abortme', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    op.drop_column('users', 'member_since')
    op.drop_column('users', 'location')
    op.drop_column('users', 'last_seen')
    op.drop_column('users', 'abortme')
    # ### end Alembic commands ###
