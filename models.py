from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def reduce(self, bank: "Bank", target: str) -> "Money":
        pass


class Money(Expression):
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def times(self, multiplier: int) -> "Money":
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend: "Money") -> "Expression":
        return Sum(self.amount + addend.amount, self.currency)

    def reduce(self, bank: "Bank", target: str) -> "Money":
        rate: bank = bank.rate(self.currency, target)
        return Money(self.amount / rate, target)

    @classmethod
    def dollar(cls, amount: int) -> "Money":
        return Money(amount, "USD")

    @classmethod
    def franc(cls, amount: int) -> "Money":
        return Money(amount, "CHF")


class Bank:
    def __init__(self) -> None:
        self.__rates: dict = {}

    def reduce(self, source: Expression, target: str) -> Money:
        return source.reduce(self, target)

    def rate(self, origin: str, target: str) -> int:
        if origin == target:
            return 1
        rate: int | None = self.__rates.get(Pair(origin, target))
        if rate is not None:
            return rate
        return 1

    def add_rate(self, origin: str, target: str, rate: int) -> None:
        self.__rates[Pair(origin, target)] = rate


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: "Bank", target: str) -> Money:
        amount = self.augend.amount + self.addend.amount
        return Money(amount, target)


class Pair:
    def __init__(self, origin: str, target: str):
        self.__origin = origin
        self.__target = target

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pair):
            return False
        return self.__origin == other.__origin and self.__target == other.__target

    def __hash__(self) -> int:
        return hash((self.__origin, self.__target))
