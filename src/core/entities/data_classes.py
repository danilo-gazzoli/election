from dataclasses import dataclass;

@dataclass
class VoterData:
    name: str;
    cardNumber: int;
    
@dataclass    
class CandidateData(VoterData):
    candidateNumer: int;
    politicalParty: str;
    typePosition: str;
    profilePicture: str; # swap to image type
    
@dataclass
class VoteData:
    voteNumber: int;
    voteType: str;
    votePosition: str;
    votePermission: bool;