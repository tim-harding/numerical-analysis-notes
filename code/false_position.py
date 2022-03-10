from math import e, fabs


def main():
    print(false_position(f, 0, 2, 30))
    print(false_position(g, -2, 0, 30))


def false_position(f, a, b, iterations):
    c = 0
    for _ in range(iterations):
        fa = f(a)
        denominator = f(b) - fa
        if fabs(denominator) < 1e-12:
            break
        c = a - fa * (b - a) / denominator
        fc = f(c)
        if fc * fa < 0:
            b = c
        else:
            a = c

    return c


def f(x):
    return 2 * x**3 - e


def g(x):
    return x**5 - x + 1


main()
