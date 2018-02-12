"""add table download 

Revision ID: 33599f9ef7fe
Revises: f1f409fc80b8
Create Date: 2018-02-12 14:15:20.259899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33599f9ef7fe'
down_revision = 'f1f409fc80b8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'download',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('download_urls', sa.ARRAY(sa.String), server_default=sa.text("array[]::varchar[]")),
        sa.Column('created_utc', sa.Integer, server_default=sa.text('extract(epoch from now())::int')),
        sa.Column('updated_utc', sa.Integer, server_default=sa.text('extract(epoch from now())::int'))
    )


def downgrade():
    op.drop_table('download')
