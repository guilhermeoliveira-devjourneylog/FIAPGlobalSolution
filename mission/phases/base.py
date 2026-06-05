from abc import ABC, abstractmethod

class MissionPhase(ABC):

    @abstractmethod
    def generate(self):
        pass