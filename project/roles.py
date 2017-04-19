from rolepermissions.roles import AbstractUserRole


class Administrator(AbstractUserRole):
    """ роль для администратора салона/филлиала """
    available_permissions = {
        'create_master': True,
        # Salon/fillial permissions
        'salon': True,
        # 'create_salon': True,
        'edit_salon': True,
        'delete_salon': True,
        # Gallery permissions
        'create_gallery': True,
        'edit_gallery': True,
        'delete_gallery': True,
        # Salon service permissions
        'create_service': True,
        'edit_service': True,
        'delete_service': True,
        # Master schedule permissions
        'edit_schedule': True,
        'delete_schedule': True,
    }


class Master(AbstractUserRole):
    """ роль для мастера салона/филлиала """
    available_permissions = {
        'profile': True,
        'edit_profile': True,
        'create_schedule': True,
        'edit_schedule': True,
        'delete_schedule': True
    }


class Moder(object):
    """
    роль для модератора всего сайта
    который может:
    утверждать пользователя на роль администратора
    исправлять/удалять данные о салоне
    исправлять/удалять галлерею
    """
    available_permissions = {
        'assign_to_administrator': True,
        # Salon permissions
        'edit_salon': True,
        'delete_salon': True,
        # Gallery permissions
        'edit_gallery': True,
        'delete_gallery': True,
        # Salon service permissions
        'edit_service': True,
        'delete_service': True,
        # Master schedule permissions
        'edit_schedule': True,
        'delete_schedule': True,
        # Post permissions
    }
