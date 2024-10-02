from src.core.entities.permission import Permission;
from src.core.interfaces.repositories.permission_repository import IPermissionRepository;

class DeletePermission:
    def __init__(self, permission_repository: IPermissionRepository, current_user):
        self._permission_repository = permission_repository;
        self._current_user = current_user;

    def execute(self, permission_id: int) -> None:
        self.verify_user_permissions(self._current_user);
        permission = self._permission_repository.GetPermissionById(permission_id);
        
        if not permission:
            raise ValueError(f"Permission with ID {permission_id} does not exist.");
        
        self.verify_permission_is_not_in_use(permission);
        self._permission_repository.DeletePermission(permission_id);

    def verify_user_permissions(user):
        if not user.is_admin():
            raise PermissionError("User does not have permission to delete a permission.");
    
    def verify_permission_is_not_in_use(permission: Permission):
        if permission.is_active:
            raise ValueError("Cannot delete an active permission.");