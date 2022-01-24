"""create all relations

Revision ID: b6ebf273e608
Revises: 1873d3eb0db6
Create Date: 2022-01-24 13:56:38.215804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6ebf273e608'
down_revision = '1873d3eb0db6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_roles',
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_users_roles_role_id_roles')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_users_roles_user_id_users'))
    )
    op.add_column('certificates', sa.Column('user_id', sa.String(length=100), nullable=False))
    op.create_foreign_key(op.f('fk_certificates_user_id_users'), 'certificates', 'users', ['user_id'], ['id'], onupdate='cascade')
    op.add_column('characteristics', sa.Column('user_id', sa.String(length=100), nullable=False))
    op.create_foreign_key(op.f('fk_characteristics_user_id_users'), 'characteristics', 'users', ['user_id'], ['id'], onupdate='cascade')
    op.add_column('groups', sa.Column('speciality_id', sa.Integer(), nullable=True))
    op.drop_constraint('groups_name_key', 'groups', type_='unique')
    op.create_unique_constraint(op.f('uq_groups_name'), 'groups', ['name'])
    op.create_foreign_key(op.f('fk_groups_speciality_id_specialitys'), 'groups', 'specialitys', ['speciality_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.add_column('payments', sa.Column('user_id', sa.String(length=100), nullable=False))
    op.create_foreign_key(op.f('fk_payments_user_id_users'), 'payments', 'users', ['user_id'], ['id'], onupdate='cascade')
    op.drop_constraint('roles_name_key', 'roles', type_='unique')
    op.create_unique_constraint(op.f('uq_roles_name'), 'roles', ['name'])
    op.drop_constraint('specialitys_code_key', 'specialitys', type_='unique')
    op.drop_constraint('specialitys_name_key', 'specialitys', type_='unique')
    op.create_unique_constraint(op.f('uq_specialitys_code'), 'specialitys', ['code'])
    op.create_unique_constraint(op.f('uq_specialitys_name'), 'specialitys', ['name'])
    op.add_column('users', sa.Column('group_id', sa.Integer(), nullable=True))
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.create_unique_constraint(op.f('uq_users_email'), 'users', ['email'])
    op.create_foreign_key(op.f('fk_users_group_id_groups'), 'users', 'groups', ['group_id'], ['id'], onupdate='cascade', ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_users_group_id_groups'), 'users', type_='foreignkey')
    op.drop_constraint(op.f('uq_users_email'), 'users', type_='unique')
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.drop_column('users', 'group_id')
    op.drop_constraint(op.f('uq_specialitys_name'), 'specialitys', type_='unique')
    op.drop_constraint(op.f('uq_specialitys_code'), 'specialitys', type_='unique')
    op.create_unique_constraint('specialitys_name_key', 'specialitys', ['name'])
    op.create_unique_constraint('specialitys_code_key', 'specialitys', ['code'])
    op.drop_constraint(op.f('uq_roles_name'), 'roles', type_='unique')
    op.create_unique_constraint('roles_name_key', 'roles', ['name'])
    op.drop_constraint(op.f('fk_payments_user_id_users'), 'payments', type_='foreignkey')
    op.drop_column('payments', 'user_id')
    op.drop_constraint(op.f('fk_groups_speciality_id_specialitys'), 'groups', type_='foreignkey')
    op.drop_constraint(op.f('uq_groups_name'), 'groups', type_='unique')
    op.create_unique_constraint('groups_name_key', 'groups', ['name'])
    op.drop_column('groups', 'speciality_id')
    op.drop_constraint(op.f('fk_characteristics_user_id_users'), 'characteristics', type_='foreignkey')
    op.drop_column('characteristics', 'user_id')
    op.drop_constraint(op.f('fk_certificates_user_id_users'), 'certificates', type_='foreignkey')
    op.drop_column('certificates', 'user_id')
    op.drop_table('users_roles')
    # ### end Alembic commands ###
