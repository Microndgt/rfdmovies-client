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
        sa.Column('release_time', sa.Date),
        sa.Column('rate', sa.Float),
        sa.Column('rate_num', sa.BigInteger),
        sa.Column('desc', sa.Text),
        sa.Column('countries', sa.ARRAY(sa.String), server_default=sa.text("array[]::varchar[]")),
        sa.Column("image_url", sa.String),
        sa.Column('types', sa.ARRAY(sa.String), server_default=sa.text("array[]::varchar[]")),
        sa.Column('director', sa.String),
        sa.Column('actors', sa.ARRAY(sa.String), server_default=sa.text("array[]::varchar[]")),
        sa.Column("douban_url", sa.String),
        sa.Column("keywords", sa.ARRAY(sa.String), server_default=sa.text("array[]::varchar[]")),
        sa.Column("languages", sa.ARRAY(sa.String), server_default=sa.text("array[]::varchar[]")),
        sa.Column("comments", sa.ARRAY(sa.String), server_default=sa.text("array[]::varchar[]")),
        sa.Column("duration", sa.Integer),
        sa.Column("grade_five", sa.Float),
        sa.Column("grade_four", sa.Float),
        sa.Column("grade_three", sa.Float),
        sa.Column("grade_two", sa.Float),
        sa.Column("grade_one", sa.Float),
        sa.Column('created_utc', sa.Integer, server_default=sa.text('extract(epoch from now())::int')),
        sa.Column('updated_utc', sa.Integer, server_default=sa.text('extract(epoch from now())::int'))
    )


def downgrade():
    op.drop_table('movie')
