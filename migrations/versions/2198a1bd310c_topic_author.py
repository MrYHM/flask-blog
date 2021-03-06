"""topic author

Revision ID: 2198a1bd310c
Revises: fb3497310380
Create Date: 2017-11-30 16:55:37.787327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2198a1bd310c'
down_revision = 'fb3497310380'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topics', sa.Column('author', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_topics_author'), 'topics', ['author'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_topics_author'), table_name='topics')
    op.drop_column('topics', 'author')
    # ### end Alembic commands ###
