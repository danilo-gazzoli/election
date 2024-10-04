import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from src.core.entities.adm import Adm;
from src.core.interfaces.repositories.adm_repository import IAdmRepository;

class GetAdm:
    def __init__(self, adm_repository: IAdmRepository):
        self._adm_repository = adm_repository;

    def execute(self, adm_id: int) -> Adm:
        adm = self._adm_repository.GetAdmById(adm_id);
        if not adm:
            raise ValueError(f"Adm with ID {adm_id} does not exist.");
        return adm;