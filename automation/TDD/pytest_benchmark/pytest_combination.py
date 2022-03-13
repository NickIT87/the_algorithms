# pytest_combination.py
import pytest


def average(n1, n2):
    return (n1 + n2) / 2


def perc_difference(n1, n2):
    return (n2 - n1)/n1 * 100


# Test the combinations of operations and inputs
@pytest.mark.parametrize("operation, n1, n2",
[(average, 1, 2), (average, 2, 3),
(perc_difference, 1, 2), (perc_difference, 2, 3)])
def test_is_float(operation, n1, n2):
    assert isinstance(operation(n1, n2), float)