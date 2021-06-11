from statistics import quantiles
# from scipy import stats


def inter_quartile(values, freqs):
    s = []
    for value, freq in zip(values, freqs):
        s += [value] * freq
        # s.extend([value] * freq) is slightly more expensive
    s.sort()
    # Should work, but hackerrank is outdated
    Q1, Q2, Q3 = [int(quartil) for quartil in quantiles(s, n=4, method="inclusive")]
    return round(float(Q3 - Q1), 1)
    # or just
    # return stats.iqr(s, interpolation='midpoint')


def main():
    int(input())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    print(inter_quartile(val, freq))


if __name__ == "__main__":
    main()
