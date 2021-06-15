from itertools import product
from random import choice


# Recursive function to return GCD(MDC) of a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# Suppose a family has 2 children, one of which is a boy(b). What is the probability that both children are boys(bb)?
def calculate_2children_prob():
    genders = ["b", "g"]
    permutation_list = list(product(genders, repeat=2))
    event_b = []
    event_bb = []
    for subset in permutation_list:
        if "b" in subset:
            event_b.append(subset)
        if ('b', 'b') == subset:
            event_bb.append(subset)
    numerator = int(len(event_bb)/gcd(len(event_bb), len(event_b)))
    denominator = int(len(event_b)/gcd(len(event_bb), len(event_b)))
    return f"{numerator}/{denominator}"
    
    # event_b = [subset for subset in permutation_list if "b" in subset]
    # event_bb = [subset for subset in event_b if ('b', 'b') == subset]
    # Is slightly slower


def choose_2children(n_simulations=100000):
    event_b = 0
    event_bb = 0
    for _ in range(n_simulations):
        child1 = choice(["b", "g"])
        child2 = choice(["b", "g"])
        children = child1 + child2
        if "b" in children:
            event_b += 1
        if children == "bb":
            event_bb += 1
    # p(b|bb) = 1
    # p(bb|b) = p(b|bb) * p(bb) / p(b)
    return event_bb/event_b


def main():
    print(calculate_2children_prob())
    print(choose_2children())
    print(round(choose_2children()*100, 2), "%")


if __name__ == "__main__":
    main()
