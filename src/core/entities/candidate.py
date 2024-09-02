from core.entities.voter import Voter;
from dataclasses import dataclass;

class CandidateData:
    candidateNumer: int;
    profilePicture: str; # swap to image type
    
class VoteData:
    voteNumber: int;
    votePermission: bool;

class Candidate(Voter):
    def __init__(self, name, cardNumber, vote_data: VoteData, candidate_data: CandidateData):
        super().__init__(name, cardNumber);
        self.candidateNumer = candidate_data.candidateNumber;
        self.profilePicture = candidate_data.profilePicture;
        self.votePermission = vote_data.votePermission;
        self.voteNumber = vote_data.voteNumber;