from core.interfaces.repositories.adm_repository import IAdmRepository;
from core.entities.adm import Adm;
from sqlalchemy.orm import Session;
from infrastructure.db.db_config import get_db_session;
from typing import Optional, List;


class CandidateRepository(IAdmRepository):
    
    def __init__(self):
        self._db_session = get_db_session;
    
    # create
    def CreateAdm(self, adm: 'Adm') -> None:
        session: Session = self._db_session();
        session.add(adm);
        session.commit();
        session.close();
        
    # read/get candidates
    def GetAdmbyID(self, adm_id: int) -> Optional['Adm']:
        session: Session = self._db_session();
        adm = session.query(Adm).filter(Adm.Id() == adm_id).first();
        session.close();
        return adm;
    
    def GetAdmbyFilter(self, **filter) -> List['Adm']:
        session: Session = self._db_session();
        adm = session.query(Adm).filter_by(**filter).all();
        session.close();
        return adm;
    
    def GetAllAdm(self) -> List['Adm']:
        session: Session = self._db_session();
        adm = session.query(Adm).all();
        session.close();
        return adm;
        
    # update
    def UpdateAdm(self, adm: 'Adm'):
        
        session: Session = self._db_session();
        existing_adm = session.query(Adm).filter(Adm.Id() == adm.Id()).first();
        
        if not existing_adm:
            raise ValueError("This adm can't be finded");
        
        existing_adm.set_name(adm.name());
        existing_adm.set_email(adm.email());
        existing_adm.set_password(adm.password());
        existing_adm.set_is_logged(adm.isLogged());
        existing_adm.set_role(adm.role());
        existing_adm.set_permition_list(adm.permitionList());
        existing_adm.set_election_list(adm.electionList());
        existing_adm.set_last_login(adm.lastLogin());
        session.commit();
        session.close();
    
    # delete
    def DeleteAdm(self, adm_id: int) -> None:
        session: Session = self._db_session();
        adm = session.query(Adm).filter(Adm.Id() == adm_id).first();

        if not adm:
            raise ValueError("Adm not finded");
        
        session.delete(adm);
        session.commit();
        session.close();