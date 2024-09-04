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
    amountVotes: int;
    profilePicture: str; # swap to image type
    
@dataclass
class VoteData:
    voteNumber: int;
    voteNull: int;
    voteNone: int;
    votePosition: str;
    votePermission: bool;
    
@dataclass
class UserData:
    id: int;
    name: str;
    email: str;
    password: str;