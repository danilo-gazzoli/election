from core.entities.data_classes import DataVoter, DataVote, DataCandidate;
from core.entities.voter import Voter;

class Candidate(Voter):
    def __init__(self, voter_data: DataVoter, vote_data: DataVote, candidate_data: DataCandidate):
        super().__init__(voter_data, vote_data, vote_data);
        self.candidateNumber = candidate_data.candidateNumber;
        self.candidateID = candidate_data.candidateID;
        self.profilePicture = candidate_data.profilePicture;
        self.politicalParty = candidate_data.politicalParty;
        self.politicalPosition = candidate_data.politicalPosition;
        self.amountVote = candidate_data.amountVotes;