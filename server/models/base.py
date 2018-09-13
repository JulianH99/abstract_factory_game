from abc import ABC, abstractmethod
from typing import Dict


class Sprite(ABC):
    """
        Class Sprite
    """
    
    _id = 0
    _sprite_name = ''

    def __init__(self):
        self._id = 0
        self._sprite_name = ''

    def get_json(self) -> Dict:
        return {
            "id": self._id,
            "sprite": self._sprite_name
        }

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
        super(Sprite, self).__init__()
        self._gender = gender
        self._sprite_name = Player.__get_body_from_gender(gender)
        self._complete_sprite_name = ''

    @staticmethod
    def __get_body_from_gender(gender: str) -> str:
        """
        Returns the sprite name for the gender given
        :param gender: the gender to be rendered
        :return: the name of the sprite
        """
        if gender == 'male':
            return "ManModel"
        else:
            return "WomanModel"

    @property
    def gender(self) -> str:
        return self._gender
    
    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def complete_sprite(self) -> str:
        return self._complete_sprite_name

    @complete_sprite.setter
    def complete_sprite(self, new_value: str):
        self._complete_sprite_name = new_value

    def get_json(self) -> Dict:
        json_dict = super(Sprite).get_json()

        json_dict['gender'] = self.gender

        return json_dict


class Pirate(Sprite):

    def __init__(self):
        super(Sprite, self).__init__()
        self._ship = None

    @property
    def ship(self):
        return self._ship

    @ship.setter
    def ship(self, ship):
        self._ship = ship

    def get_json(self) -> Dict:
        json_dict = super().get_json()
        json_dict['ship'] = self._ship.get_json()
        return json_dict


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
