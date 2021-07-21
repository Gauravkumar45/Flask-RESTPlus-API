"""empty message

Revision ID: a60851e7652d
Revises: f8836ae1185f
Create Date: 2021-05-20 23:01:26.235993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a60851e7652d'
down_revision = 'f8836ae1185f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicles', sa.Column('owner', sa.String(length=50), nullable=True))
    op.add_column('vehicles', sa.Column('contact', sa.String(length=50), nullable=True))
    op.add_column('vehicles', sa.Column('address', sa.String(length=50), nullable=True))
    op.add_column('vehicles', sa.Column('ownership', sa.Boolean(), server_default='false', nullable=True))
    op.drop_column('vehicles', 'vcontact')
    op.drop_column('vehicles', 'vownership')
    op.drop_column('vehicles', 'vaddress')
    op.drop_column('vehicles', 'vowner')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicles', sa.Column('vowner', sa.VARCHAR(length=50), nullable=True))
    op.add_column('vehicles', sa.Column('vaddress', sa.VARCHAR(length=50), nullable=True))
    op.add_column('vehicles', sa.Column('vownership', sa.BOOLEAN(), server_default=sa.text("'false'"), nullable=True))
    op.add_column('vehicles', sa.Column('vcontact', sa.VARCHAR(length=50), nullable=True))
    op.drop_column('vehicles', 'ownership')
    op.drop_column('vehicles', 'address')
    op.drop_column('vehicles', 'contact')
    op.drop_column('vehicles', 'owner')
    # ### end Alembic commands ###