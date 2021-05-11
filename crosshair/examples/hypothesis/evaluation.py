# Tests that won't find bugs in hypothesis, but will find bugs when run with crosshair.


import hypothesis.strategies as st
from hypothesis import given


@given(st.integers())
def test_div_zero(x):
    1 / (x - 13242)


@given(st.integers(), st.integers(min_value=-100000))
def test_multiple_strategies(x, y):
    1 / (x + y + 2300)


@given(st.integers(2).map(lambda x: x * x))
def test_map(x):
    assert x % 1098567819578 != 1


@given(st.integers(1).map(lambda x: x * 2))
def test_one_of(x):
    assert x % 2 == 0
    assert x % 2 == 1


def multiply_2(x):
    return x * 2


@given(st.integers(1).map(multiply_2))
def test_one_of_alt(x):
    assert x % 2 == 0
    assert x % 2 == 1


# TODO: Fix bug with getting lambda source when we have 2 or lambda expressions with the same variable in a contract.
# Causes flaky erroneous behaviour with the below tests.


@given(st.integers().map(lambda x: x - 5), st.integers().map(lambda x: x - 23))
def test_multi_map(x, y):
    1 / (x + y - 3920001)


@given(
    st.one_of(
        st.integers().map(lambda x: x * 2), st.integers().map(lambda x: x * 2 + 1)
    )
)
def test_one_of_with_map(x):
    assert x % 2 == 0


@given(st.one_of(st.integers().map(multiply_2)))
def test_bar(x):
    assert x % 2 == 0
    assert x % 2 == 1