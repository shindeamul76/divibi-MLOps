"""Update existing records and set merkle_root as non-nullable

Revision ID: 9d43f4ef75d0
Revises: b6c595a00c2e
Create Date: 2024-09-24 00:51:03.944092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d43f4ef75d0'
down_revision = 'b6c595a00c2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('model_metadata', schema=None) as batch_op:
        batch_op.alter_column('merkle_root',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('model_metadata', schema=None) as batch_op:
        batch_op.alter_column('merkle_root',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)

    # ### end Alembic commands ###
