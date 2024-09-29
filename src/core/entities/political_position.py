from dataclasses import dataclass;
from candidate import Candidate;
from typing import List;

@dataclass
class PoliticalPosition:
    _id: int; 
    _name: str;
    _vacancies: int; 
    _candidatesCompeting: List['Candidate'];
        
    # political postion id getter 
    @property
    def Id(self):
        return self._id;
    
    # political postion getter and setter
    @property
    def name(self):
        return self._name;
    
    @name.setter
    def set_name(self, value):
        if not value:
            raise ValueError("Name can't be empty");
        self._name = value;
    
    # political postion vacancies getter and setter
    @property
    def vacancies(self):
        return self._vacancies;
    
    @vacancies.setter
    def set_vacancies(self, value: int):
        if value < 1:
            return;
        self._vacancies = value;
    
    # political position candidates competing getter and setter
    @property
    def candidatesCompeting(self):
        return self._candidatesCompeting;
    
    @candidatesCompeting.setter
    def set_candidatesCompeting(self, candidates: List['Candidate']):
        
        if not all(isinstance(candidate, Candidate) for candidate in candidates):
            raise ValueError("All candidates must be instances of Candidate");
        
        self._candidatesCompeting = candidates;