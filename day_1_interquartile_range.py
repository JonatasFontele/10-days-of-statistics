import statistics


def inter_quartile(values, freqs):
    s = [values * freqs for values, freqs in zip(values, freqs)]
    s.sort()
    Q1, Q2, Q3 = [quartil for quartil in statistics.quantiles(s)]
    return round(Q3 - Q1, 1)


def main():
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    print(inter_quartile(val, freq))


if __name__ == "__main__":
    main()
