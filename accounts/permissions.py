from rolepermissions.checkers import has_role
from project.roles import Administrator


def access_create_master(user):
    if has_role(user, [Administrator]):
        return True
    return False
