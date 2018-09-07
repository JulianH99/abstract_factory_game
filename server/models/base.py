from abc import ABC, abstractmethod


class Sprite(ABC):
    """
        Class Sprite
    """
    
    _id = 0
    _sprite_name = ''

    def __init__(self):
        self._id = 0
        self._sprite_name = ''

    @abstractmethod
    def get_json(self): pass

    @property
    def id(self) -> int:
        return self._id

    @property
    def sprite_name(self) -> str:
        return self._sprite_name

    @sprite_name.setter
    def sprite_name(self, new_sprite_name):
        
        self._sprite_name = new_sprite_name


class Player(Sprite):

    def __init__(self, gender):
        self._gender = gender

    @property
    def gender(self) -> str:
        return self._gender
    
    @gender.setter
    def gender(self, value):
        self._gender = value

    def get_json(self):
        name = self.sprite_name
        id = self.id
        gender = self.gender
        
        return {"name": name, "id": id, "gender": gender}


class Pirate(Sprite):

    def __init__(self):
        self._ship = None

    @property
    def ship(self):
        return self._ship

    @ship.setter
    def ship(self, ship):
        self._ship = ship

    def get_json(self):
        return {
            'ship': self._ship.get_json()
        }


class User:
    __name: str
    __player: Player

    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if new_name == '':
            raise Exception("User name cannot be empty")
        self.__name = new_name
