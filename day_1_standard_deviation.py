from math import sqrt
from statistics import mean


def std_dev(arr):
    average = mean(arr)
    return round(sqrt(sum((val - average) ** 2 for val in arr) / len(arr)), 1)
    # or
    # return round(statistics.pstdev(arr), 1)
    # pstdev is population standard deviation, while stdev is sample standard deviation len(arr)-1


def main():
    int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    print(std_dev(vals))


if __name__ == "__main__":
    main()
