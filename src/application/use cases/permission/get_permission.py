from src.core.entities.permission import Permission;
from src.core.interfaces.repositories.permission_repository import IPermissionRepository;

class GetPermission:
    def __init__(self, permission_repository: IPermissionRepository):
        self._permission_repository = permission_repository;

    def execute(self, permission_id: int) -> Permission:
        permission = self._permission_repository.GetPermissionById(permission_id);
        if not permission:
            raise ValueError(f"Permission with ID {permission_id} does not exist.");
        return permission;
