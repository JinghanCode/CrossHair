import hypothesis.strategies as st
from hypothesis import given


@given(st.integers(0, 116))
def test_integers_bounded(x):
    1 / (x - 117)


@given(st.integers(1,5))
def zac_test(x):
    assert 1 <= x <= 5


@given(st.integers(min_value=1, max_value=5), st.integers(min_value=-100000, max_value=-1000))
def test_multiple_strategies(x, y):
    1 / (x + y)

def some_func(x):
    return x * 2


@given(st.integers(2, 2).map(some_func))
def test_map(x):
    assert x == 0

