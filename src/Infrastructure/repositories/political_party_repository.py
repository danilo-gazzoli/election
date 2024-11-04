import sys;
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')));
from core.interfaces.repositories.political_party_repository import IPoliticalPartyRepository;
from core.entities.political_party import PoliticalParty;
from sqlalchemy.orm import Session;
from infrastructure.db.db_config import get_db_session;
from typing import Optional, List;

class PoliticalPartyRepository(IPoliticalPartyRepository):
    
    def __init__(self) -> None:
        self._db_session = lambda: next(get_db_session);
        
    # create
    def CreatePoliticalParty(self, politicalParty: 'PoliticalParty') -> None:
        session: Session = self._db_session();
        session.add(politicalParty);
        session.commit();
        session.close();
    
    # read
    def GetPoliticalPartybtId(self, politicalParty_id: int) -> Optional['PoliticalParty']:
        session: Session = self._db_session();
        politicalParty = session.query(PoliticalParty).filter(PoliticalParty.Id() == politicalParty_id).first();
        session.close();
        return politicalParty;
        
    def GetPoliticalPartybyFilter(self, **filter) -> List['PoliticalParty']:
        session: Session = self._db_session();
        politicalParty = session.query(PoliticalParty).filter_by(**filter).all();
        session.close();
        return politicalParty;
    
    def GetAllPoliticalPartys(self) -> List['PoliticalParty']:
        session: Session = self._db_session();
        politicalParty = session.query(PoliticalParty).all();
        session.close();
        return politicalParty;
    
    # update
    def UpdatePoliticalParty(self, politicalParty: 'PoliticalParty') -> None:
        session: Session = self._db_session();
        existing_politicalParty = session.query(PoliticalParty).filter(PoliticalParty.Id() == politicalParty.Id()).first();
        
        if not existing_politicalParty:
            raise ValueError("This political party can't be finded");
        
        existing_politicalParty.set_name(politicalParty.name());
        existing_politicalParty.set_picture(politicalParty.picture());
        existing_politicalParty.set_candidate_list(politicalParty.candidatesList());
        
        session.commit();
        session.close();
        
    # delete
    def DeletePoliticalParty(self, politicalParty_id: int) -> None:
        session: Session = self._db_session();
        existing_politicalParty = session.query(PoliticalParty).filter(PoliticalParty.Id() == politicalParty_id).first();
        
        if not existing_politicalParty:
            raise ValueError("This political party can't be finded");
        
        session.delete(existing_politicalParty);
        session.commit();
        session.close();