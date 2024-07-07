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
        return Money(self.amount + addend.amount, self.currency)

    @classmethod
    def dollar(self, amount: int) -> "Money":
        return Money(amount, "USD")

    @classmethod
    def franc(cls, amount: int) -> "Money":
        return Money(amount, "CHF")


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return Money.dollar(10)
