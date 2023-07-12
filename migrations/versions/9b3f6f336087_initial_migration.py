"""Initial migration

Revision ID: 9b3f6f336087
Revises: 
Create Date: 2023-07-08 11:27:17.880317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b3f6f336087'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('asset_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('asset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('asset_name', sa.String(length=100), nullable=False),
    sa.Column('serial_number', sa.String(length=50), nullable=False),
    sa.Column('purchase_date', sa.DateTime(), nullable=False),
    sa.Column('purchase_cost', sa.Float(), nullable=False),
    sa.Column('current_value', sa.Float(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('assigned_to', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['assigned_to'], ['user.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['asset_category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('serial_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('asset')
    op.drop_table('asset_category')
    op.drop_table('user')
    # ### end Alembic commands ###