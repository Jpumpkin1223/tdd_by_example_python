class Dollor:
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int) -> "Dollor":
        return Dollor(self.amount * multiplier)

    def equals(self, other: "Dollor") -> bool:
        return self.amount == other.amount
