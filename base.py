# def my_sum(a, b, c):
#     return a + b + c


def my_sum(a, b, c):
    return sum([a, b, c])


def test_sum():
    assert my_sum(1, 1, 1) == 3
