from core.entities.voter import Voter

class Candidate(Voter):
    def __init__(self, name, cardNumber, candidateNumber, profilePicture):
        super().__init__(name, cardNumber);
        self.__candidateNumer = candidateNumber;
        self.__profilePicture = profilePicture;

