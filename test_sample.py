# pytest example
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_answer2():
    assert func(4) == 5


def test_answer3():
    assert func(4) == 5


def test_answer4():
    assert func(2) == 5
