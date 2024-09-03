from abc import ABC, abstractmethod;
from core.entities.data_classes import VoteData;
from typing import Optional, List;


class IVoteRepository(ABC):
    @abstractmethod
    def GetVotesbyCandidate(candidate_id: int) -> List[VoteData]:
        pass;
    
    @abstractmethod
    def GetVotesbyPoliticalParty(politicalParty: str) -> List[VoteData]:
        pass;
    
    @abstractmethod
    def GetVotesbyVoteType(voteType: str) -> List[VoteData]:
        pass;
    
    @abstractmethod
    def GetTotalVotes() -> int:
        pass;
    
    @abstractmethod
    def GetVotesbyPoliticalPosition(politicalPosition: str) -> List[VoteData]:
        pass;