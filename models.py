class Dollor:
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int) -> "Dollor":
        return Dollor(self.amount * multiplier)
