from dataclasses import dataclass;
from political_position import PoliticalPosition;
from entities.political_party import PoliticalParty;
from entities.election import Election;
from entities.voter import Voter;
from PIL import Image; 

@dataclass
class Candidate(Voter):
    _candidateID: int;
    _candidateNumber: int;
    _candidade_politicalParty: 'PoliticalParty';
    _candidade_politicalPosition: 'PoliticalPosition';
    _amountVotes: int;
    _profilePicture: Image;
        
    # candidate number getter and setter
    @property
    def candidateNumber(self):
        return self._candidateNumber;
    
    @candidateNumber.setter
    def set_candidate_number(self, value: int, election: 'Election'):
        
        if value is None:
            raise ValueError("The candidate number can't be empty");
        
        for candidate in election.ElectionCandidates():
            if candidate.CandidateNumber() == value:
                raise ValueError(f"Candidate number {value} is already use by another candidate");

        self._candidateNumber = value;
        
    # candidate political position getter and setter
    @property
    def politicalPosition(self) -> 'PoliticalPosition':
        return self._candidade_politicalPosition;
    
    @politicalPosition.setter
    def set_candidate_political_position(self, value: 'PoliticalPosition'):
        if not isinstance(value, PoliticalPosition):
            raise ValueError("Invalid political position")
        self._candidade_politicalPosition = value;
    
    # candidate political party getter and setter
    @property
    def politicalParty(self) -> 'PoliticalParty':
        return self._candidade_politicalParty;
            
    @politicalParty.setter
    def set_candidate_political_party(self, value: 'PoliticalParty', political_position: 'PoliticalPosition'):
        
        political_postion_vacancies = PoliticalPosition.vacancies();
        
        if value is None:
            raise ValueError("The political party can't be empty");
        
        if (political_postion_vacancies < 2):
            
            for candidates in PoliticalPosition.candidatesCompeting():
                
                if Candidate.CandidatePoliticalPosition == value:
                    raise ValueError("This political position don't allows competition between candidates from the same party");
                
            return;
        
        self._candidade_politicalParty = value;
        
    # candidate amount vote getter and setter
    @property
    def amountVote(self): 
        return self._amountVote;
    
    @amountVote.setter
    def set_candidate_amount_vote(self, value: int):
        
        if value < 0:
            raise ValueError("Amount votes can't be negative");
        
        self._amountVote = value;
        
    # candidate profile picture getter and setter
    @property
    def profilePicture(self) -> Image:
        return self._profilePicture;
    
    @profilePicture.setter
    def set_profilePicture(self, value: Image):
        
        if value is None:
            raise ValueError("The profile picture can't be empty");
        
        self._profilePicture = value;