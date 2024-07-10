"""Updated all to handle many-many relationships

Revision ID: 8732c920c72d
Revises: 19e76915174c
Create Date: 2024-07-10 11:34:13.908807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8732c920c72d'
down_revision = '19e76915174c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chapter', schema=None) as batch_op:
        batch_op.drop_constraint('chapter_event_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('chapter_magic_system_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('chapter_faction_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('chapter_location_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('chapter_creature_id_fkey', type_='foreignkey')
        batch_op.drop_column('location_id')
        batch_op.drop_column('creature_id')
        batch_op.drop_column('magic_system_id')
        batch_op.drop_column('faction_id')
        batch_op.drop_column('event_id')

    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_type', sa.String(length=50), nullable=False))
        batch_op.drop_column('type')

    with op.batch_alter_table('system', schema=None) as batch_op:
        batch_op.drop_constraint('system_world_id_fkey', type_='foreignkey')
        batch_op.drop_column('world_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('system', schema=None) as batch_op:
        batch_op.add_column(sa.Column('world_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('system_world_id_fkey', 'world', ['world_id'], ['id'])

    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
        batch_op.drop_column('item_type')

    with op.batch_alter_table('chapter', schema=None) as batch_op:
        batch_op.add_column(sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('faction_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('magic_system_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('creature_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('location_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('chapter_creature_id_fkey', 'creature', ['creature_id'], ['id'])
        batch_op.create_foreign_key('chapter_location_id_fkey', 'location', ['location_id'], ['id'])
        batch_op.create_foreign_key('chapter_faction_id_fkey', 'faction', ['faction_id'], ['id'])
        batch_op.create_foreign_key('chapter_magic_system_id_fkey', 'system', ['magic_system_id'], ['id'])
        batch_op.create_foreign_key('chapter_event_id_fkey', 'event', ['event_id'], ['id'])

    # ### end Alembic commands ###
