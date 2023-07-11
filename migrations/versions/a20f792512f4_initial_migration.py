"""Initial migration

Revision ID: a20f792512f4
Revises: b505cce2ea46
Create Date: 2023-07-11 21:44:38.845145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a20f792512f4'
down_revision = 'b505cce2ea46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asset_category', schema=None) as batch_op:
        batch_op.drop_constraint('asset_category_parent_category_id_fkey', type_='foreignkey')
        batch_op.drop_column('parent_category_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asset_category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('parent_category_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('asset_category_parent_category_id_fkey', 'asset_category', ['parent_category_id'], ['id'])

    # ### end Alembic commands ###
