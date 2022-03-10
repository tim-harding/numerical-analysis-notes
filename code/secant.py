from math import e, fabs


def main():
    print(secant(f, -1/2, 1/2, 30))
    print(secant(g, -1, -2, 30))


def secant(f, x0, x1, iterations):
    for _ in range(iterations):
        fx0 = f(x0)
        den = f(x1) - fx0
        if fabs(den) < 1e-12:
            break
        x2 = x0 - fx0 * (x1 - x0) / den
        x0 = x1
        x1 = x2
    return x0


def f(x):
    return 2 * x**3 - e


def g(x):
    return x**5 - x + 1


main()
