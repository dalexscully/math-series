def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    if n <= 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0, y=1):
    if x == 0 and y == 1:
        return fibonacci(n)
    elif x == 2 and y == 1:
        return lucas(n)

