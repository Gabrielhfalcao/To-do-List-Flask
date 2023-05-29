"""empty message

Revision ID: 9a19113134d4
Revises: 85b758e055e5
Create Date: 2023-05-25 21:53:51.199544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a19113134d4'
down_revision = '85b758e055e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tituloTarefa', sa.String(), nullable=True),
    sa.Column('descricaoTarefa', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('tituloTarefa', sa.VARCHAR(), nullable=True),
    sa.Column('descricaoTarefa', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('tasks')
    # ### end Alembic commands ###
