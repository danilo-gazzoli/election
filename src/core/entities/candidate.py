from dataclasses import dataclass;
from entities.political_party import PoliticalParty;
from entities.election import Election;
from PIL import Image; 

@dataclass
class Candidate():
    _candidateId: int;
    _name: str;
    _cardNumber: int;
    _candidateNumber: int;
    _candidade_politicalParty: 'PoliticalParty';
    _amountVotes: int;
    _profilePicture: Image;
    
    # candidate id getter
    @property
    def Id(self):
        return self._candidateId;
    
    # candidate card number getter and setter
    @property
    def cardNumber(self):
        return self._cardNumber;
    
    @cardNumber.setter
    def set_card_number(self, value: int):
        self._cardNumber = value;
        
    # candidate name getter and setter
    @property
    def name(self):
        return self._name;
    
    @name.setter
    def set_name(self, value: str):
        self._name = value;    
    
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
    
    
    # candidate political party getter and setter
    @property
    def politicalParty(self) -> 'PoliticalParty':
        return self._candidade_politicalParty;
            
    @politicalParty.setter
    def set_candidate_political_party(self, value: 'PoliticalParty'):
                
        if value is None:
            raise ValueError("The political party can't be empty");
        
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