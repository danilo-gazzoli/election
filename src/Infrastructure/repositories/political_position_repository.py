from core.interfaces.repositories.political_position_repository import IPoliticalPositionRepository;
from core.entities.permission import Permission;
from sqlalchemy.orm import Session;
from Infrastructure.db.db import get_db_session;
from typing import Optional, List

from src.core.entities.political_position import PoliticalPosition;

class PoliticalPositionRepository(IPoliticalPositionRepository):
    
    def __init__(self):
        self._db_session = get_db_session;
        
    # create
    def CreatePoliticalPosition(self, politicalPosition: 'PoliticalPosition'):
        session: Session = self._db_session();
        session.add(politicalPosition);
        session.commit();
        
    # read
    def GetPoliticalPositionbyID(self, politicalPosition_id: int) -> 'PoliticalPosition' | None:
        session: Session = self._db_session();
        return session.query(PoliticalPosition).fiter(PoliticalPosition.Id() == politicalPosition_id).first();
    
    def GetPoliticalPositionbyFilter(self, **filter) -> List['PoliticalPosition']:
        session: Session = self._db_session();
        return session.query(PoliticalPosition).filter_by(**filter).all();
    
    def GetAllPoliticalPositions(self) -> List['PoliticalPosition']:
        session: Session = self._db_session();
        return session.query(PoliticalPosition).all();
    
    # update
    def UpdatePoliticalPosition(self, politicalPosition: 'PoliticalPosition'):
        session: Session = self._db_session();
        existing_politicalPosition = session.query(PoliticalPosition).filter(PoliticalPosition.Id() == politicalPosition.Id()).first();
        
        if not existing_politicalPosition:
            raise ValueError("This political position can't be finded");

        existing_politicalPosition.set_name(politicalPosition.name());
        existing_politicalPosition.set_vacancies(politicalPosition.vacancies());
        existing_politicalPosition.set_candidatesCompeting(politicalPosition.candidatesCompeting());

    # delete
    def DeletePoliticalPosition(self, politicalPosition_id: int) -> None:
        session: Session = self._db_session();
        existing_politicalPosition = session.query(PoliticalPosition).filter(PoliticalPosition.Id() == politicalPosition_id).first();
        
        if not existing_politicalPosition:
            raise ValueError("This political position can't be finded");
        
        session.delete(existing_politicalPosition);
        session.commit();