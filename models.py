# from abc import ABCMeta, abstractmethod


class Money:
    def __init__(self, amount: int):
        self._amount = amount

    @classmethod
    def dollar(cls, amount: int) -> "Dollar":
        return Dollar(amount)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        print(type(self), type(other))
        return self._amount == other._amount and type(self) == type(other)


class Dollar(Money):
    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
