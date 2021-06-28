from itertools import product
from random import randint


# Recursive function to return GCD(MDC) of a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def calculate_dice_prob():
    numbers = [1, 2, 3, 4, 5, 6]
    # Specify the number of characters that each combination has
    permutation_list = list(product(numbers, repeat=2))
    # tuple returned with a match per loop
    event_list = [subset for subset in permutation_list if subset[0] + subset[1] == 6]
    numerator = int(len(event_list)/gcd(len(event_list), len(permutation_list)))
    denominator = int(len(permutation_list)/gcd(len(event_list), len(permutation_list)))
    # For fractional representation
    return f"{numerator}/{denominator}"


def roll_the_dice(n_simulations=100000):
    count = 0
    for _ in range(n_simulations):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        score = die1 + die2
        if score == 6:
            count += 1
    return count/n_simulations


def main():
    print(calculate_dice_prob())
    print(roll_the_dice())
    print(round(roll_the_dice()*100, 2), "%")


if __name__ == "__main__":
    main()
