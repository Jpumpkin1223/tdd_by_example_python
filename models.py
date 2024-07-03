class Dollor:
    def __init__(self, amount: int):
        self.__amount = amount

    def __eq__(self, other) -> bool:
        if not isinstance(other, Dollor):
            return False
        return self.__amount == other.__amount

    def times(self, multiplier: int) -> "Dollor":
        return Dollor(self.__amount * multiplier)


class Franc:
    def __init__(self, amount: int):
        self.__amount = amount

    def __eq__(self, other) -> bool:
        if not isinstance(other, Franc):
            return False
        return self.__amount == other.__amount

    def times(self, multiplier: int) -> "Franc":
        return Franc(self.__amount * multiplier)
