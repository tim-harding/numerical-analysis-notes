from math import fabs


def main():
    print(fixed_point(g, 0, 1e-6))


def fixed_point(g, x, max_error):
    error = 1000000000
    while error > max_error:
        previous_x = x
        x = g(x)
        error = fabs(x - previous_x)
    return x


def g(x):
    """Fixed point iteration of second root for 0 = -4x^2 - 3x + 1"""
    return 1 / (4 * x + 3)


main()