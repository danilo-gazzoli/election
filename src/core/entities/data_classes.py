from dataclasses import dataclass;

@dataclass
class VoterData:
    name: str;
    cardNumber: int;
    
@dataclass    
class CandidateData(VoterData):
    candidateID: int;
    candidateNumber: int;
    politicalParty: str;
    politicalPosition: str;
    profilePicture: str; # swap to image type
    
@dataclass
class VoteData:
    voteNumber: int;
    voteType: str;
    votePosition: str;
    votePermission: bool;