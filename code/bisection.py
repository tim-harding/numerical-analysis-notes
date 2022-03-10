import math


def main():
    print(bisection(f, -1, 0, 1e-6))
    print(bisection(f, 0, 1.333, 1e-6))
    print(bisection(f, 1.333, 2, 1e-6))


def bisection(f, a, b, max_error):
    steps = math.ceil(math.log((b - a) / max_error - 1, 2))
    fa = f(a)
    for _ in range(steps):
        c = (b + a) / 2
        fc = f(c)
        if fc * fa < 0:
            b = c
        else:
            a = c
    return a


def f(x):
    return x * x * x - 2 * x * x + 1


main()
