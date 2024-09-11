from core.entities.data_classes import DataVoter, DataVote, DataCandidate;
from core.entities.political_position import PoliticalPosition;
from core.entities.political_party import PoliticalParty;
from core.entities.election import Election;
from core.entities.voter import Voter;

class Candidate(Voter):
    def __init__(self, voter_data: DataVoter, vote_data: DataVote, candidate_data: DataCandidate):
        super().__init__(voter_data, vote_data);
        self._candidateNumber = candidate_data.candidateNumber;
        self._candidateID = candidate_data.candidateID;
        self._profilePicture = candidate_data.profilePicture;
        self._politicalParty = candidate_data.politicalParty;
        self._politicalPosition = candidate_data.politicalPosition;
        self._amountVote = candidate_data.amountVotes;
        
    # candidate card number getter and setter
    @property
    def cardNumber(self):
        return self._cardNumber;
    
    @cardNumber.setter
    def set_card_number(self, value: int):
        
        if value is None:
            raise ValueError("Card number can't be empty");
        
        self._cardNumber = value;
        
    # candidate name getter and setter
    @property
    def name(self):
        return self._name;
    
    @name.setter
    def set_name(self, value: str):
        
        if value is None:
            raise ValueError("Name can't be empty");
        
        self._name = value;
        
    # candidate vote number getter and setter
    @property
    def voteNumber(self):
        return self._voteNumber
    
    @voteNumber.setter
    def set_vote_number(self, value):
        self._voteNumber = value;
        
    # candidate vote permission getter and setter
    @property
    def votePermission(self):
        return self._votePermission
    
    @votePermission.setter
    def set_vote_permission(self, value: bool):
        self._votePermission = value;
        
    # candidate vote position getter and setter
    @property
    def votePosition(self):
        return self._voteNumber
    
    @votePosition.setter
    def set_vote_position(self, value: str):
        
        if value is None:
            raise ValueError("Vote position can't be empty");
        
        self._votePosition = value;
        
    # candidate number getter and setter
    @property
    def candidateNumber(self):
        return self._candidateNumber;
    
    @candidateNumber.setter
    def set_candidate_number(self, value: int, election: Election):
        
        if value is None:
            raise ValueError("The candidate number can't be empty");
        
        for candidate in election.ElectionCandidates():
            if candidate.CandidateNumber() == value:
                raise ValueError(f"Candidate number {value} is already use by another candidate");

        self._candidateNumber = value;
        
    # candidate political position getter and setter
    @property
    def politicalPosition(self) -> PoliticalPosition:
        return self._politicalPosition;
    
    @politicalPosition.setter
    def set_candidate_political_position(self, value: PoliticalPosition):
        if not isinstance(value, PoliticalPosition):
            raise ValueError("Invalid political position")
        self._politicalPosition = value;
    
    # candidate political party getter and setter
    @property
    def politicalParty(self) -> PoliticalParty:
        return self._politicalParty;
            
    @politicalParty.setter
    def set_candidate_political_party(self, value: PoliticalParty, political_position: PoliticalPosition):
        
        political_postion_vacancies = PoliticalPosition.vacancies();
        
        if value is None:
            raise ValueError("The political party can't be empty");
        
        if (political_postion_vacancies < 2):
            
            for candidates in PoliticalPosition.candidatesCompeting():
                
                if Candidate.CandidatePoliticalPosition == value:
                    raise ValueError("This political position don't allows competition between candidates from the same party");
                
            return;
        
        self._politicalParty = value;
        
    # candidate amount vote getter and setter
    @property
    def amountVote(self): 
        return self._amountVote;
    
    @amountVote.setter
    def set_candidate_amount_vote(self, value: int):
        
        if value < 0:
            raise ValueError("Amount votes can't be negative");
        
        self._amountVote = value;