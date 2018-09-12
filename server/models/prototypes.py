from abc import ABC, abstractclassmethod
from .factories.sprite_factories import PirateFactory
from copy import deepcopy

class AbstractProtorype(ABC):
    
    @abstractclassmethod
    def clone(cls):
        pass

class PiratePrototype(AbstractProtorype):
    __pirate_instance = None

    @abstractclassmethod
    def clone(cls):
        if cls.__pirate_instance is None:
            cls.__pirate_instance = PirateFactory.factory_method()
        return deepcopy(cls.__pirate_instance)
        
        

