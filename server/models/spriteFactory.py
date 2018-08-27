from abc import ABC, abstractmethod


class SpriteFactory(ABC):
    """
    Class spriteFactory
    """

    @abstractmethod
    def factoryMethod(self):
        pass
