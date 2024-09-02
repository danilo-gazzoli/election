from dataclasses import dataclass;

class CandidateData:
    candidateNumer: int;
    profilePicture: str; # swap to image type
    
class VoterData:
    name: str;
    cardNumber: int;

    
class VoteData:
    voteNumber: int;
    votePermission: bool;