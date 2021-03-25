import hypothesis.strategies as st
from hypothesis import given

# This test should pass.
@given(st.integers(0, 116))
def test_integers_bounded(x):
    1 / (x - 117)

# This should pass.
@given(st.integers(1,5))
def zac_test(x):
    assert 1 <= x <= 5

