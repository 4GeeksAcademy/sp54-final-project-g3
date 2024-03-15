"""empty message

Revision ID: 07d87bc3c7bd
Revises: aa2ca4818958
Create Date: 2024-03-15 20:12:27.773346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07d87bc3c7bd'
down_revision = 'aa2ca4818958'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainers_classes', schema=None) as batch_op:
        batch_op.drop_constraint('trainers_classes_date_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainers_classes', schema=None) as batch_op:
        batch_op.create_unique_constraint('trainers_classes_date_key', ['date'])

    # ### end Alembic commands ###