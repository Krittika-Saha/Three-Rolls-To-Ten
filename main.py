from itertools import permutations
import random

# Input
sides_of_die_1 = int(input("Custom sides of die: "))
number_of_rolls_1 = int(
    input("Number of rolls taken to reach the desired number: "))
end_number_1 = int(input("End number that one has to reach to win: "))
trials = int(input("Number of trials for experimental probability: "))


# Theoretical permutation function
def theoretical_probability(sides_of_die=6, number_of_rolls=3, end_number=10):
    """Gives the theoretical probabilty of winning the game of the number of rolls to a particular number"""
    string = ''
    for i in range(sides_of_die + 1):
        if i != 0:
            string += str(i)
    win = 0
    lose = 0
    no_of_permutations = list(permutations(string, number_of_rolls))
    attempts = len(no_of_permutations)
    for i in no_of_permutations:
        add = 0
        for j in i:
            add += int(j)
        if add >= end_number:
            win += 1
        else:
            lose += 1
    try:
        return round((win / attempts) * 100, 2)
    except ZeroDivisionError:
        return 0


# Experimental Probability function
def experimental_probability(sides_of_die=6, number_of_rolls=3, end_number=10, number_of_trials=100):
    """Gives the experimental probability that can be customised by the number of trials"""
    smallest_number = '1'
    largest_number = '9'
    for k in range(number_of_rolls-1):
        smallest_number += '0'
        largest_number += '9'
    win = 0
    lose = 0
    for j in range(number_of_trials):
        add_result = 0
        random_number = str(random.randint(int(smallest_number), int(largest_number)))
        for i in random_number:
            while int(i) > sides_of_die or int(i) == 0:
                random_number = list(str(random.randint(int(smallest_number), int(largest_number))))
                i = random_number[0]
        for j in random_number:
            add_result += int(j)
        if add_result >= end_number:
            win += 1
        else:
            lose += 1
        win_percent = round((win / number_of_trials) * 100, 2)
    return win_percent

# Calling of functions
win_chance_theoretical = theoretical_probability(sides_of_die_1, number_of_rolls_1, end_number_1)
win_chance_experimental = experimental_probability(sides_of_die_1, number_of_rolls_1, end_number_1, trials)
print(f"{win_chance_theoretical}, {win_chance_experimental}")
