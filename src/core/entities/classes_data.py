from dataclasses import dataclass;
from datetime import datetime
from typing import List;
from PIL import Image;

@dataclass
class DataVoter:
    name: str;
    cardNumber: int;
    
@dataclass    
class DataCandidate(DataVoter):
    from political_party import PoliticalParty;
    from political_position import PoliticalPosition;
    
    candidateID: int;
    candidateNumber: int;
    politicalParty: 'PoliticalParty';
    politicalPosition: 'PoliticalPosition';
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
class DataAdm(DataUser):
    adminRole: str;
    permissionsList: List[str];
    lastLogin: datetime;

@dataclass
class DataPermission():
    id: int;
    name: str;
    description: str;
    accessLevels: List[str];
    isActive: bool;
    
@dataclass
class DataPoliticalParty:
    from political_party import PoliticalParty;
    from candidate import Candidate;
    
    id: int;
    name: str;
    partyPicture: Image;
    candidateList: List['Candidate'];
    
@dataclass
class DataPoliticalPosition:
    from political_position import PoliticalPosition;
    from candidate import Candidate;
    
    id: int;
    name: str;
    vacancies: int;
    candidatesCompeting: List['Candidate'];
    
@dataclass
class DataElection:
    from political_position import PoliticalPosition;
    from political_party import PoliticalParty;
    from candidate import Candidate;
    from voter import Voter;
    
    id: int;
    name: str;
    politicalPositions: List['PoliticalPosition'];
    politicalCandidates: List['Candidate'];
    politicalPartys: List['PoliticalParty'];
    voters: List['Voter'];
    