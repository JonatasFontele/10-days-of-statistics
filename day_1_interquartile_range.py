import statistics


def inter_quartile(values, freqs):
    s = []
    for values, freqs in zip(values, freqs):
        for _ in range(freqs):
            s.append(values)
    print(s)
    s.sort()
    print(s)
    Q1, Q2, Q3 = [quartil for quartil in statistics.quantiles(s, n=4, method="inclusive")]
    print(Q1)
    print(Q2)
    print(Q3)
    return round(Q3 - Q1, 1)


def main():
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    print(inter_quartile(val, freq))


if __name__ == "__main__":
    main()
