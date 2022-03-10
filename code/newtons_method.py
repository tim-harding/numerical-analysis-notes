from math import fabs


def main():
    print(newtons_iteration(f, df, -1, 1e-6))
    print(newtons_iteration(f, df, 1/2, 1e-6))
    print(newtons_iteration(f, df, 2, 1e-6))


def f(x):
    return x * x * x - 2 * x * x + 1


def df(x):
    return 3 * x * x - 4 * x


def newtons_iteration(f, df, x, epsilon):
    error = 100000000000
    while error > epsilon:
        previous_x = x
        x = x - f(x) / df(x)
        error = fabs(previous_x - x)
    return x


main()
