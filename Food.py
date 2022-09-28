import abc
import math


class Food(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def applyFood(self, critter):
        raise NotImplementedError


class Banana:
    def applyFood(self, critter):
        critter.change_food(1)


class Poison:
    def applyFood(self, critter):
        critter.change_food(100)


