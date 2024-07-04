from models import Dollar, Franc, Money


def test_dollor_multiplication() -> None:
    five: Dollar = Money.dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)


def test_franc_multiplication() -> None:
    five: Franc = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)


def test_equality() -> None:
    assert Dollar(5) == Dollar(5)
    assert not Dollar(5) == Dollar(6)
    assert Franc(5) == Franc(5)
    assert not Franc(5) == Franc(6)
    assert not Dollar(5) == Franc(5)
