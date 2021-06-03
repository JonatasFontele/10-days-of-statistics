# import statistics
# from scipy import stats
from collections import Counter


def mean(x):
    # return round(statistics.mean(x), 1)
    # or
    return round(sum(x) / len(x), 1)


def median(x):
    # return round(statistics.median(x), 1)
    # or
    # floor division operator // to get an integer and use it as an index
    index = len(x) // 2
    # Sample with an odd number of observations
    if len(x) % 2:
        return round(sorted(x)[index], 1)
    # Sample with an even number of observations
    return round(sum(sorted(x)[index - 1:index + 1]) / 2, 1)


def mode(x):
    # return int(stats.mode(x)[0])
    # or
    count = Counter(sorted(x))
    # most_common(number of tuples)[list index][tuple index]
    mode_list = [key for key, value in count.items() if value == count.most_common(1)[0][1]]
    return mode_list[0]


def validate(n, x):
    constraints = True
    for number in x:
        if not (number in range(1, 10 ** 5 + 1)):
            constraints = False
            break
    if constraints and 10 <= n <= 2500:
        print(mean(x))
        print(median(x))
        print(mode(x))


def main():
    n = int(input())
    x = list(map(int, input().split()))
    validate(n, x)


if __name__ == "__main__":
    main()
