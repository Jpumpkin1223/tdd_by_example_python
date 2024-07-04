class Money:
    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        print(type(self), type(other))
        return self._amount == other._amount and type(self) == type(other)


class Dollor(Money):
    def times(self, multiplier: int) -> "Dollor":
        return Dollor(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int) -> "Franc":
        return Franc(self._amount * multiplier)
