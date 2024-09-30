from core.interfaces.repositories.adm_repository import IAdmRepository;
from core.entities.adm import Adm;
from sqlalchemy.orm import Session;
from Infrastructure.db.db import get_db_session;
from typing import Optional, List;


class CandidateRepository(IAdmRepository):
    
    def __init__(self):
        self._db_session = get_db_session;
    
    # create
    def CreateAdm(self, adm: 'Adm') -> None:
        session: Session = self._db_session();
        session.add(adm);
        session.commit();
        
    # read/get candidates
    def GetAdmbyID(self, adm_id: int) -> Optional['Adm']:
        session: Session = self._db_session();
        return session.query(Adm).filter(Adm.Id() == adm_id).first();
    
    def GetAdmbyFilter(self, **filter) -> List['Adm']:
        session: Session = self._db_session();
        return session.query(Adm).filter_by(**filter).all();
    
    def GetAllAdm(self) -> List['Adm']:
        session: Session = self._db_session();
        return session.query(Adm).all();
        
    # update
    def UpdateAdm(self, adm: 'Adm'):
        
        session: Session = self._db_session();
        existing_adm = session.query(Adm).filter(Adm.Id() == adm.Id()).first();
        
        if not existing_adm:
            raise ValueError("This adm can't be finded");
        
        existing_adm._name = adm.name();
        existing_adm._email = adm.email();
        existing_adm._password = adm.password();
        existing_adm._isLogged = adm.isLogged();
        existing_adm._adminRole = adm.role();
        existing_adm._permitionsList = adm.permitionList();
        existing_adm._electionList = adm.electionList();
        existing_adm._lastLogin = adm.lastLogin();
        session.commit();
    
    # delete
    def DeleteAdm(self, adm_id: int) -> None:
        session: Session = self._db_session();
        adm = session.query(Adm).filter(Adm.Id() == adm_id).first();

        if adm:
            session.delete(adm);
            session.commit();