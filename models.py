class Expression:
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

    @classmethod
    def dollar(cls, amount: int) -> "Money":
        return Money(amount, "USD")

    @classmethod
    def franc(cls, amount: int) -> "Money":
        return Money(amount, "CHF")


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        if isinstance(source, Money):
            return source
        sum: Sum = source
        return sum.reduce(to)


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str) -> Money:
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)
