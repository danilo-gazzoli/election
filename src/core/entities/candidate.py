from core.entities.data_classes import *;
from core.entities.voter import Voter;

class Candidate(Voter):
    def __init__(self, voter_data: VoterData, vote_data: VoteData, candidate_data: CandidateData):
        super().__init__(voter_data, vote_data, vote_data);
        self.candidateNumber = candidate_data.candidateNumber;
        self.profilePicture = candidate_data.profilePicture;
        self.politicalParty = candidate_data.politicalParty;
        self.typePosition = candidate_data.typePosition;