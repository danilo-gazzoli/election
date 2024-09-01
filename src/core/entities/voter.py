from dataclasses import dataclass

class VoterData:
    name: str
    cardNumber: int

class Voter:
    def __init__(self, voter_data: VoterData):
        self.__cardNumber = voter_data.cardNumber;
        self.__name = voter_data.name;