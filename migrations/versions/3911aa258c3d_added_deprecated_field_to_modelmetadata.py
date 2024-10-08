"""Added deprecated field to ModelMetadata

Revision ID: 3911aa258c3d
Revises: 65be8ac06445
Create Date: 2024-09-28 01:57:33.717928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3911aa258c3d'
down_revision = '65be8ac06445'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('model_metadata', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deprecated', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('model_metadata', schema=None) as batch_op:
        batch_op.drop_column('deprecated')

    # ### end Alembic commands ###
