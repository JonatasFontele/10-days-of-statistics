from itertools import product
from fractions import Fraction
from random import choice


# Suppose a family has 2 children, one of which is a boy(b). What is the probability that both children are boys(bb)?
def calculate_2children_prob():
    genders = ["b", "g"]
    cartesian_product_list = list(product(genders, repeat=2))
    event_b = []
    event_bb = []
    for subset in cartesian_product_list:
        if "b" in subset:
            event_b.append(subset)
        if ('b', 'b') == subset:
            event_bb.append(subset)
    return Fraction(len(event_bb), len(event_b))

    # event_b = [subset for subset in cartesian_product_list if "b" in subset]
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
