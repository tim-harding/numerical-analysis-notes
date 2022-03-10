def main():
    print(expected(100))
    print(actual(100))


def expected(N):
    return N * (N + 1) * (2*N + 1) // 6 + N * (N + 1) // 2


def actual(N):
    count = 0
    for m in range(1, N + 1):
        for q in range(1, m + 2):
            for p in range(1, m + 1):
                count += 1
    return count


main()
