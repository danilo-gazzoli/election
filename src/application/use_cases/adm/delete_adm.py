import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from core.interfaces.repositories.adm_repository import IAdmRepository;

class DeleteAdm:
    def __init__(self, adm_repository: IAdmRepository, current_user):
        self._adm_repository = adm_repository;
        self._current_user = current_user;

    def execute(self, adm_id: int) -> None:
        self.verify_user_permissions(self._current_user);
        adm = self._adm_repository.GetAdmById(adm_id);
        
        if not adm:
            raise ValueError(f"Adm with ID {adm_id} does not exist.");
        
        self._adm_repository.DeleteAdm(adm_id)
    
    def verify_user_permissions(self, user):
        if not user.is_admin():
            raise PermissionError("User does not have permission to delete an admin.");
