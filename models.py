from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount: int):
        self._amount = amount

    @classmethod
    def dollar(cls, amount: int) -> "Money":
        return Dollar(amount)

    @classmethod
    def franc(cls, amount: int) -> "Money":
        return Franc(amount)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        print(type(self), type(other))
        return self._amount == other._amount and type(self) == type(other)

    @abstractmethod
    def times(self, multiplier: int) -> "Money":
        pass


class Dollar(Money):
    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
