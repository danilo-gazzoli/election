from src.core.entities.election import Election
from src.core.interfaces.repositories.election_repository import IElectionRepository;
from core.entities.adm import Adm;
from sqlalchemy.orm import Session;
from Infrastructure.db.db import get_db_session;
from typing import Optional, List;

class ElectionRepository(IElectionRepository):
    
    def __init__(self):
        self._db_session = get_db_session;
        
    # create
    def CreateElection(self, election: 'Election') -> None:
        session: Session = self._db_session();
        session.add(election);
        session.commit();
    
    # read
    def GetElectionbyID(self, election_id: int) -> 'Election' | None:
        session: Session = self._db_session();
        return session.query(Election).filter(Election.Id() == election_id).first();
    
    def GetElectionbyFilter(self, **filter) -> List['Election']:
        session: Session = self._db_session();
        return session.query(Election).filter_by(**filter).all();
    
    def GetAllElections(self) -> List[Election]:
        session: Session = self._db_session();
        return session.query(Adm).all();
    
    # update
    def UpdateElection(self, election: 'Election'):
        session: Session = self._db_session();
        existing_election = session.query(Election).filter(Election.Id() == election.Id()).first();
        
        if not existing_election:
            raise ValueError("This election can't be finded");
        
        existing_election.candidates = election.candidates();
        existing_election.name = election.name();
        existing_election.politicalPartys = election.politicalPartys();
        existing_election.politicalPositions = election.politicalPositions();
        existing_election.usersRegistered = election.usersRegistered();
        
    
    # delete
    def DeleteElection(self, election_id: int) -> None:
        session: Session = self._db_session();
        election = session.query(Election).filter(Election.Id() == election_id).first();
        
        if not election:
            raise ValueError("This election can't be finded");
        
        session.delete(election);
        session.commit();