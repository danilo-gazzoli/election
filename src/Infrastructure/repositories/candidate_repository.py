from core.interfaces.repositories.candidate_repository import ICandidateRepository;
from core.entities.candidate import Candidate;
from sqlalchemy.orm import Session;
from Infrastructure.db.db import get_db_session;
from typing import Optional, List;


class CandidateRepository(ICandidateRepository):
    
    def __init__(self):
        self._db_session = get_db_session;
    
    # create
    def CreateCandidate(self, candidate: 'Candidate') -> None:
        session: Session = self._db_session();
        session.add(candidate);
        session.commit();
        
    # read/get candidates
    def GetCandidatebyID(self, candidate_id: int) -> Optional['Candidate']:
        session: Session = self._db_session();
        return session.query(Candidate).filter(Candidate.Id() == candidate_id).first();
    
    def GetCandidatebyFilter(self, **filter) -> List['Candidate']:
        session: Session = self._db_session();
        return session.query(Candidate).filter_by(**filter).all();
    
    def GetAllCandidate(self) -> List['Candidate']:
        session: Session = self._db_session();
        return session.query(Candidate).all();
        
    # update
    def UpdateCandidate(self, candidate: 'Candidate'):
        
        session: Session = self._db_session();
        existing_candidate = session.query(Candidate).filter(Candidate.Id() == candidate.Id()).first();
        
        if not existing_candidate:
            raise ValueError("This candidate can't be finded");
        
        existing_candidate.name = candidate.name();
        existing_candidate.cardNumber = candidate.cardNumber();
        existing_candidate.candidateNumber = candidate.candidateNumber();
        existing_candidate.amountVote = candidate.amountVote();
        existing_candidate.profilePicture = candidate.profilePicture();
        session.commit();
    
    # delete
    def DeleteCandidate(self, candidate_id: int) -> None:
        session: Session = self._db_session();
        candidate = session.query(Candidate).filter(Candidate.Id() == candidate_id).first();

        if candidate:
            session.delete(candidate);
            session.commit();