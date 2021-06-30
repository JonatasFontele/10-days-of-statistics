from itertools import product
from fractions import Fraction
from random import randint


def calculate_dice_prob():
    numbers = [1, 2, 3, 4, 5, 6]
    # Specify the number of characters that each combination has
    permutation_list = list(product(numbers, repeat=2))
    # P(A and B) = P(A | B) * P(B) = 4/5 * 5/36 = 4/36 = 1/9
    event_list = [subset[0] + subset[1] == 6 and subset[0] != subset[1] for subset in permutation_list]
    return Fraction(event_list.count(True), len(event_list))


def roll_the_dice(n_simulations=100000):
    count = 0
    for _ in range(n_simulations):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        score = die1 + die2
        if score == 6 and die1 != die2:
            count += 1
    return count/n_simulations


def main():
    print(calculate_dice_prob())
    print(roll_the_dice())
    print(round(roll_the_dice()*100, 2), "%")


if __name__ == "__main__":
    main()
