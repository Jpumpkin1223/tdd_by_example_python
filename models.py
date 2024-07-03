class Dollor:
    def __init__(self, amount: int):
        self.amount = amount

    def __eq__(self, other) -> bool:
        if not isinstance(other, Dollor):
            return False
        return self.amount == other.amount

    def times(self, multiplier: int) -> "Dollor":
        return Dollor(self.amount * multiplier)
