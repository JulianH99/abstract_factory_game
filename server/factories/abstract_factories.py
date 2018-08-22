from abc import ABC, abstractmethod
from ..models.sprites.players import _Player

class AbstractFactory(ABC):

    @abstractmethod
    def create_player(player: str) -> _Player :
        pass
    
