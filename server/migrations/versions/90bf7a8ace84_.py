"""empty message

Revision ID: 90bf7a8ace84
Revises: 
Create Date: 2019-11-13 00:30:39.566707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90bf7a8ace84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('errors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_errors_registered_at'), 'errors', ['registered_at'], unique=False)
    op.create_table('redirects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_redirects_registered_at'), 'redirects', ['registered_at'], unique=False)
    op.create_table('urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('short_url', sa.String(length=10), nullable=True),
    sa.Column('long_url', sa.String(length=400), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_urls_long_url'), 'urls', ['long_url'], unique=True)
    op.create_index(op.f('ix_urls_short_url'), 'urls', ['short_url'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urls_short_url'), table_name='urls')
    op.drop_index(op.f('ix_urls_long_url'), table_name='urls')
    op.drop_table('urls')
    op.drop_index(op.f('ix_redirects_registered_at'), table_name='redirects')
    op.drop_table('redirects')
    op.drop_index(op.f('ix_errors_registered_at'), table_name='errors')
    op.drop_table('errors')
    # ### end Alembic commands ###
