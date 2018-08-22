from abc import ABC, abstractmethod
from typing import List


class _Player(ABC):
    _name: str = ''
    _life_points: int = 0
    _experience_points: int = 0
    _artifacts: List[int] = []
    _gender: str = ''


class MalePlayer(_Player):
    """
    Class MalePlayer
    """
    def __init__(self, name: str):
        self._artifacts = []
        self._name = name
        self._life_points = 100
        self._experience_points = 0
        self._gender = 'M'


class FemalePlayer(_Player):
    def __init__(self, name: str):
        self._artifacts = []
        self._name = name
        self._life_points = 100
        self._experience_points = 0
        self._gender = 'F'
    


