from core.entities.data_classes import VoterData, VoteData, CandidateData;
from core.entities.voter import Voter;

class Candidate(Voter):
    def __init__(self, voter_data: VoterData, vote_data: VoteData, candidate_data: CandidateData):
        super().__init__(voter_data, vote_data, vote_data);
        self.candidateNumber = candidate_data.candidateNumber;
        self.candidateID = candidate_data.candidateID;
        self.profilePicture = candidate_data.profilePicture;
        self.politicalParty = candidate_data.politicalParty;
        self.amountVote = candidate_data.amountVotes;
        self.politicalPosition = candidate_data.politicalPosition;