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


# This should fail with x in [1,5]
@given(st.integers(1, 5))
def test_integers_bounded(x):
    assert x == 10


# This should fail with x = 117.
@given(st.integers(0, 118))
def test_integers_bounded_alternate(x):
    1 / (x - 117)


# This should fail with x = 3,4,5
@given(st.integers(1, 5))
def zac_test(x):
    assert 1 <= x <= 2


# This should fail with x + y = 0
@given(st.integers(min_value=1, max_value=5), st.integers(min_value=-100000))
def test_multiple_strategies(x, y):
    1 / (x + y)


@given(st.one_of(st.integers(1, 5), st.integers(9, 10)))
def test_integers_union(x):
    assert x >= 1
    assert x <= 10
    assert x == 6

def map_to_one(x):
    return 

@given(
    st.one_of(
        st.integers(1, 5), st.integers(9, 10)
        )
    )
def test_integers_union_map(x):
    assert x >= 1
    assert x <= 10
    assert x == 6 

