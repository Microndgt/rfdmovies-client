"""init db

Revision ID: f1f409fc80b8
Revises: 
Create Date: 2018-02-12 09:57:33.656298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1f409fc80b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'movie',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('release_time', sa.DateTime),
        sa.Column('rate', sa.Float),
        sa.Column('rate_num', sa.BigInteger),
        sa.Column('desc', sa.Text),
        sa.Column('country', sa.String),
        sa.Column('type', sa.ARRAY(sa.String)),
        sa.Column('director', sa.String),
        sa.Column('actor', sa.ARRAY(sa.String)),
        sa.Column("link", sa.String),
        sa.Column('created_utc', sa.Integer, server_default=sa.text('extract(epoch from now())::int')),
        sa.Column('updated_utc', sa.Integer, server_default=sa.text('extract(epoch from now())::int'))
    )


def downgrade():
    op.drop_table('movie')
