import sys;
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')));

from core.interfaces.repositories.candidate_repository import ICandidateRepository;
from core.entities.candidate import Candidate;
from sqlalchemy.orm import Session;
from Infrastructure.db.db_config import get_db_session;
from typing import Optional, List;


class CandidateRepository(ICandidateRepository):
    
    def __init__(self):
        self._db_session = get_db_session;
    
    # create
    def CreateCandidate(self, candidate: 'Candidate') -> None:
        session: Session = self._db_session();
        session.add(candidate);
        session.commit();
        session.close();
        
    # read/get candidates
    def GetCandidatebyID(self, candidate_id: int) -> Optional['Candidate']:
        session: Session = self._db_session();
        candidate = session.query(Candidate).filter(Candidate.Id() == candidate_id).first();
        session.close();
        return candidate;
    
    def GetCandidatebyFilter(self, **filter) -> List['Candidate']:
        session: Session = self._db_session();
        candidate = session.query(Candidate).filter_by(**filter).all();
        session.close();
        return candidate;
    
    def GetAllCandidate(self) -> List['Candidate']:
        session: Session = self._db_session();
        candidate = session.query(Candidate).all();
        session.close();
        return candidate;
        
    # update
    def UpdateCandidate(self, candidate: 'Candidate'):
        
        session: Session = self._db_session();
        existing_candidate = session.query(Candidate).filter(Candidate.Id() == candidate.Id()).first();
        
        if not existing_candidate:
            raise ValueError("This candidate can't be finded");
        
        existing_candidate.set_name(candidate.name());
        existing_candidate.set_card_number(candidate.cardNumber());
        existing_candidate.set_candidate_number(candidate.candidateNumber());
        existing_candidate.set_candidate_political_party(candidate.politicalParty());
        existing_candidate.set_candidate_political_position(candidate.politicalPosition());
        existing_candidate.set_candidate_amount_vote(candidate.amountVote());
        existing_candidate.set_profilePicture(candidate.profilePicture());
        session.commit();
        session.close();
    
    # delete
    def DeleteCandidate(self, candidate_id: int) -> None:
        session: Session = self._db_session();
        candidate = session.query(Candidate).filter(Candidate.Id() == candidate_id).first();

        if not candidate:
            raise ValueError("Candidate not finded");
        
        session.delete(candidate);
        session.commit();
        session.close();