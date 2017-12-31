"""empty message

Revision ID: 619fb8c4e2a4
Revises: 
Create Date: 2017-12-30 00:08:25.769222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '619fb8c4e2a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bucketlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bucketlists')
    # ### end Alembic commands ###
