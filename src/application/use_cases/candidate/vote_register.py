import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'));
sys.path.append(src_path);
from core.entities.election import Election;
from src.core.interfaces.repositories.candidate_repository import ICandidateRepository;
from src.core.interfaces.repositories.election_repository import IElectionRepository;

class VoteRegister:
    def __init__(self, candidate_repository: 'ICandidateRepository', election_repository: 'IElectionRepository') -> None:
        self._candidate_repository = candidate_repository;
        self._election_repository = election_repository;
        
    def execute(self, candidate_id: int | None, election_id: int):
        if election_id is None:
            raise ValueError("Election id can't be null");
        
        candidate = self._candidate_repository.GetCandidatebyID(candidate_id);
        
        if not candidate:
            raise ValueError("Candidate not founded in database");
        
        if candidate_id is not None:
            atual_amount_votes = candidate.amountVote();
            atual_amount_votes += 1;
            candidate.set_candidate_amount_vote(atual_amount_votes);
        
            self._candidate_repository.UpdateCandidate(candidate);
            
            return;
        
        election = self._election_repository.GetElectionbyID(election_id);
            
        none_votes = election.noneVotes();
        
        none_votes += 1;
        
        election.set_none_votes(none_votes);
        
        self._election_repository.UpdateElection(election);
        
        
        
        
        