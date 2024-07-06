class Money:
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> "Money":
        return Money(self._amount * multiplier, self._currency)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount and self._currency == other._currency

    @classmethod
    def dollar(cls, amount: int) -> "Money":
        return Dollar(amount, "USD")

    @classmethod
    def franc(cls, amount: int) -> "Money":
        return Franc(amount, "CHF")


class Dollar(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)


class Franc(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)
