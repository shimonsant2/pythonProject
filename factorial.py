def func(n):
    if n < 1:
        return 0
    print(n)
    return func(n - 1)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
func(3)
