import hypothesis.strategies as st
from hypothesis import given

# This should fail with x as any integer.
@given(st.integers())
def test_integers_minimal(x):
    assert False

# This test should fail with x = 0
@given(st.integers())
def test_integers_basic(x):
    1 / x

# This should fail with x = 117.
@given(st.integers(0, 118))
def test_integers_bounded(x):
    1 / (x - 117)

# This should fail with x = 3,4,5
@given(st.integers(1, 5))
def zac_test(x):
    assert 1 <= x <= 2



