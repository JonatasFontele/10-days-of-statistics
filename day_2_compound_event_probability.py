from itertools import product
from fractions import Fraction
from random import choice


def calculate_urn_prob():
    X = ["b", "b", "b", "r", "r", "r", "r"]
    Y = ["b", "b", "b", "b", "r", "r", "r", "r", "r"]
    Z = ["b", "b", "b", "b", "r", "r", "r", "r"]
    # Urn X has a 4/7 probability of giving a red ball
    # Urn Y has a 5/9 probability of giving a red ball
    # Urn Z has a 1/2 probability of giving a red ball
    #
    # Urn X has a 3/7 probability of giving a black ball
    # Urn Y has a 4/9 probability of giving a black ball
    # Urn Z has a 1/2 probability of giving a black ball
    permutation_list = list(product(X, Y, Z))

    # P(2 red, 1 black)
    # P(Red Red Black) + P(Red Black Red) + P(Black Red Red)
    event_list = [subset.count("r") == 2 for subset in permutation_list]
    return Fraction(event_list.count(True), len(event_list))


def draw_from_urn(n_simulations=100000):
    event = 0
    for _ in range(n_simulations):
        X = choice(["b", "b", "b", "r", "r", "r", "r"])
        Y = choice(["b", "b", "b", "b", "r", "r", "r", "r", "r"])
        Z = choice(["b", "b", "b", "b", "r", "r", "r", "r"])
        urns = X + Y + Z
        if urns.count("r") == 2:
            event += 1
    return event / n_simulations


def main():
    print(calculate_urn_prob())
    print(draw_from_urn())
    print(round(draw_from_urn()*100, 2), "%")


if __name__ == "__main__":
    main()
