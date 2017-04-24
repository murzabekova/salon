from rolepermissions.permissions import register_object_checker
from project.roles import Administrator


@register_object_checker()
def access_create_master(user):
    if user.role == 'administrator':
        return True
