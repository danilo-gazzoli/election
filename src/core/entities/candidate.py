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
    def CandidateCardNumber(self):
        return self._cardNumber;
    
    @CandidateCardNumber.setter
    def set_card_number(self, value: int):
        
        if value is None:
            raise ValueError("Card number can't be empty");
        
        self._cardNumber = value;
        
    # candidate name getter and setter
    @property
    def CandidateName(self):
        return self._name;
    
    @CandidateName.setter
    def set_name(self, value: str):
        
        if value is None:
            raise ValueError("Name can't be empty");
        
        self._name = value;
        
    # candidate vote number getter and setter
    @property
    def CandidateVoteNumber(self):
        return self._voteNumber
    
    @CandidateVoteNumber.setter
    def set_vote_number(self, value: int):
        self._voteNumber = value;
        
    # candidate vote permission getter and setter
    @property
    def CandidateVotePermission(self):
        return self._votePermission
    
    @CandidateVotePermission.setter
    def set_vote_permission(self, value: bool):
        self._votePermission = value;
        
    # candidate vote position getter and setter
    @property
    def CandidateVotePosition(self):
        return self._voteNumber
    
    @CandidateVotePosition.setter
    def set_vote_position(self, value: str):
        
        if value is None:
            raise ValueError("Vote position can't be empty");
        
        self._votePosition = value;
        
    # candidate number getter and setter
    @property
    def CandidateNumber(self):
        return self._candidateNumber;
    
    @CandidateNumber.setter
    def set_candidate_number(self, value: int, election: Election):
        
        if value is None:
            raise ValueError("The candidate number can't be empty");
        
        for candidate in election.ElectionCandidates():
            if candidate.CandidateNumber() == value:
                raise ValueError(f"Candidate number {value} is already use by another candidate");

        self._candidateNumber = value;
        
    # candidate political position getter and setter
    @property
    def CandidatePoliticalPosition(self) -> PoliticalPosition:
        return self._politicalPosition;
    
    @CandidatePoliticalPosition.setter
    def set_candidate_political_position(self, value: PoliticalPosition):
        if not isinstance(value, PoliticalPosition):
            raise ValueError("Invalid political position")
        self._politicalPosition = value;
    
    # candidate political party getter and setter
    @property
    def CandidatePoliticalParty(self) -> PoliticalParty:
        return self._politicalParty;
            
    @CandidatePoliticalParty.setter
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
    def CandidateAmountVote(self): 
        return self._amountVote;
    
    @CandidateAmountVote.setter
    def set_candidate_amount_vote(self, value: int):
        
        if value < 0:
            raise ValueError("Amount votes can't be negative");
        
        self._amountVote = value;