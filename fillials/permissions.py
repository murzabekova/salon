from rolepermissions.permissions import register_object_checker
from project.roles import Administrator


@register_object_checker()
def access_salon(role, user):
    if role == Administrator:
        return True
    return False


@register_object_checker()
def access_gallery(role, user):
    if role == Administrator:
        return True
    return False


@register_object_checker()
def access_services(role, user):
    if role == Administrator:
        return True
    return False


@register_object_checker()
def access_accounts(role, user):
    if role == Administrator:
        return True
    return False
