from statistics import median


def quartiles(arr):
    arr.sort()
    Q1 = median(arr[:len(arr)//2])
    Q2 = median(arr)
    if len(arr) % 2:
        Q3 = median(arr[len(arr) // 2 + 1:])
    else:
        Q3 = median(arr[len(arr) // 2:])
    print(int(Q1))
    print(int(Q2))
    print(int(Q3))
    # or
    # return [print(int(quartil)) for quartil in statistics.quantiles(arr)]
    # Quartiles go from 1 to 4 and Quantiles can go from anything to anything.
    # The default quantiles() is to set n to 4 (quartiles)


def main():
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    quartiles(data)


if __name__ == "__main__":
    main()
