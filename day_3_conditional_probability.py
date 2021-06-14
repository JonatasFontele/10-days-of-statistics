from itertools import product
import random


# Recursive function to return GCD(MDC) of a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?
def calculate_2children_prob():
    genders = ["b", "g"]
    permutation_list = list(product(genders, repeat=2))
    sample_space = [subset for subset in permutation_list if "b" in subset]
    event_list = [subset for subset in sample_space if ('b', 'b') == subset]
    numerator = int(len(event_list)/gcd(len(event_list), len(sample_space)))
    denominator = int(len(sample_space)/gcd(len(event_list), len(sample_space)))
    return f"{numerator}/{denominator}"


def choose_2children(n_simulations=100000):
    event = 0
    sample = 0
    for _ in range(n_simulations):
        child1 = random.choice(["b", "g"])
        child2 = random.choice(["b", "g"])
        children = child1 + child2
        if "b" in children:
            sample += 1
        if children == "bb":
            event += 1
    return event/sample


def main():
    print(calculate_2children_prob())
    print(choose_2children())
    print(round(choose_2children()*100, 2), "%")


if __name__ == "__main__":
    main()
