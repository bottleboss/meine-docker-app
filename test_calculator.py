# test_calculator.py
from calculator import add

def test_add_positive_numbers():
    """Testet die Addition von zwei positiven Zahlen."""
    # Expectation: 2 + 3 sollte 5 sein.
    # Reality: Das Ergebnis von add(2, 3)
    assert add(2, 3) == 5

def test_add_with_error():
    """Dieser Test soll bewusst fehlschlagen."""
    # Expectation: 5 + 5 sollte 10 sein. Wir behaupten fälschlicherweise, es sei 9.
    # Reality: Das Ergebnis von add(5, 5)
    assert add(5, 5) == 10
