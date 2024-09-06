from core.entities.political_position import PoliticalPosition;
from core.entities.political_party import PoliticalParty;
from core.entities.candidate import Candidate;
from core.entities.voter import Voter;
from core.entities.user import User;
from dataclasses import dataclass;
from typing import List;
from PIL import Image;

@dataclass
class DataVoter:
    name: str;
    cardNumber: int;
    
@dataclass    
class DataCandidate(DataVoter):
    candidateID: int;
    candidateNumber: int;
    politicalParty: str;
    politicalPosition: str;
    amountVotes: int;
    profilePicture: Image;
    
@dataclass
class DataVote:
    voteNumber: int;
    voteNull: int;
    voteNone: int;
    votePosition: str;
    votePermission: bool;
    
@dataclass
class DataUser:
    id: int;
    name: str;
    email: str;
    password: str;
    
@dataclass
class DataPoliticalParty:
    id: int;
    name: str;
    partyPicture: Image;
    candidateList: List[Candidate];
    
@dataclass
class DataPoliticalPosition:
    id: int;
    name: str;
    candidatesCompeting: List[Candidate];
    
@dataclass
class DataElection:
    id: int;
    name: str;
    politicalPositions: List[PoliticalPosition];
    politicalCandidates: List[Candidate];
    politicalPartys: List[PoliticalParty];
    voters: List[Voter];
    