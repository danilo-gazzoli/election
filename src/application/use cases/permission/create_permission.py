from core.interfaces.repositories.permission_repository import IPermissionRepository;
from core.entities.permission import Permission;

class CreateUser:
    def __init__(self, PermissionRepository: IPermissionRepository):
        self._permission_repository = PermissionRepository;
        
    def execute(self, permission_data: dict) -> None:
        permission = Permission(
            name = permission_data['name'],
            description = permission_data['description'],
            accessLevels = permission_data['accessLevels'],
            isActive = permission_data['isActive']
        )

        self._permission_repository.CreateUser(permission);