# Tests that won't find bugs in hypothesis, but will find bugs when run with crosshair.


import hypothesis.strategies as st
from hypothesis import given


# @given(st.integers())
# def test_div_zero(x):
#     1 / (x - 13242)
#
#
# @given(st.integers(), st.integers(min_value=-100000))
# def test_multiple_strategies(x, y):
#     1 / (x + y + 2300)
#

def multiply_2(x):
    return x * 2


# @given(st.integers(2).map(lambda x: x*x))
# def test_map(x):
#     assert x % 1098567819578 != 1



@given(st.integers(1).map(lambda x: x*2))
def test_one_of(x):
    assert x % 2 == 0
    assert x % 2 == 1
