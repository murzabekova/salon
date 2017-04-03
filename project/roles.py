from rolepermissions.roles import AbstractUserRole


class Administrator(AbstractUserRole):
    available_permissions = {
        'create_master': True,
        'edit_salon': True,
        'delete_salon': True,
    }


class Master(AbstractUserRole):
    available_permissions = {
        'create_master_profile': True,
        'edit_master_profile': True,
        'create_master_gallery': True,
        'add_master_gallery_image': True,
    }
