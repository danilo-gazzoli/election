from core.interfaces.repositories.adm_repository import IAdmRepository;
from core.entities.adm import Adm;

class CreateUser:
    def __init__(self, AdmRepository: IAdmRepository):
        self._adm_repository = AdmRepository;
        
    def execute(self, adm_data: dict) -> None:
        adm = Adm(
            name = adm_data['name'],
            email = adm_data['email'],
            password = adm_data['password'],
            isLogged = adm_data['isLogged'],
            isLogged = adm_data['isLogged'],
            adminRole = adm_data['adminRole'],
            permitionList = adm_data['permitionList'],
            electionList = adm_data['electionList'],
            lastLogin = adm_data['lastLogin']
        )

        self._adm_repository.CreateUser(adm);