# pytest example
def func(x):
    return x + 1


def test_answer1():
    assert func(3) == 5


def test_answer2():
    assert func(3) == 4
