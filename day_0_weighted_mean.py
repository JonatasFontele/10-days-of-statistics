# import numpy as np


def weighted_mean(x, w):
    # Zip() returns a list of tuples, where an i-th tuple contains the i-th element of each of the arguments.
    return round(sum(val * weight for val, weight in zip(x, w)) / sum(w), 1)
    # or
    # return round(np.average([x], weights=[w]), 1)


def main():
    int(input())
    vals = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    print(weighted_mean(vals, weights))


if __name__ == "__main__":
    main()
