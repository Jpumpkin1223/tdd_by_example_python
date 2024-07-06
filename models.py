from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def currency(self) -> str:
        return self._currency

    @classmethod
    def dollar(cls, amount: int) -> "Money":
        return Dollar(amount, "USD")

    @classmethod
    def franc(cls, amount: int) -> "Money":
        return Franc(amount, "CHF")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        print(type(self), type(other))
        return self._amount == other._amount and type(self) == type(other)

    @abstractmethod
    def times(self, multiplier: int) -> "Money":
        pass


class Dollar(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> Money:
        return Money.dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> Money:
        return Money.franc(self._amount * multiplier)
