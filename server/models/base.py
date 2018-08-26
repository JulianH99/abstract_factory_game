from abc import ABC, abstractmethod


class Sprite(ABC):
    """
        Class Sprite
    """
    __id: int
    __sprite_name: str

    @abstractmethod
    def get_json(self): pass

    @property
    def id(self) -> int:
        return self.__id

    @property
    def sprite_name(self) -> str:
        return self.__sprite_name

    @sprite_name.setter
    def sprite_name(self, new_sprite_name):
        if new_sprite_name == '':
            raise Exception("sprite name cannot be empty")
        self.__sprite_name = new_sprite_name


class Player(Sprite):

    __gender: str

    def __init__(self, gender):
        self.__gender = gender

    def get_json(self):
        pass


class User:
    __name: str
    __player: Player

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if new_name == '':
            raise Exception("User name cannot be empty")
        self.__name = new_name
