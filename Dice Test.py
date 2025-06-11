import random
from collections import defaultdict

from enum import IntEnum
class Die(IntEnum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20

def roll_exploding_die(die: Die) -> int:
    """Rolls an exploding die. If the max value is rolled, it rolls again and adds the result."""
    exploding_die_total = 0
    sides = die.value
    roll = sides
    while roll == sides:
        roll = random.randint(1, sides)
        exploding_die_total += roll
    return exploding_die_total

def roll_morph_die(starting_die: Die):
    """
    Rolls a morph die, progressing up the chain on a max roll.
    Terminates if a natural 20 is rolled on a d20.
    """

    morph_die_total = 0

    for die in Die:
        if die is not starting_die:
            continue

        sides = die.value
        roll = random.randint(1, sides)
        morph_die_total += roll

        if roll != sides:
            break # terminate roll sequence

    return morph_die_total

def simulate_rolls(dice, modifier=0, dc=10, trials=100000, use_morph_die=True, starting_morph_die=Die.D4):
    """
    Simulates a number of dice rolls to determine success rate

    Parameters:
    -dice: potential values that can be rolled, representing different die (e.g., [4] for 1d4, [6] for 1d6, etc)
    -modifier: static bonus to the roll (default 0, could be 1, 2, 3, etc)
    -dc: difficulty class to meet or beat
    -trials: simulations ran
    -use_morph_die: whether to add one morph die to each roll
    """

    successes = 0
    results_distribution = defaultdict(int)

    for _ in range(trials):
        total = 0
        for num_sides in dice:
            roll_result = roll_exploding_die(num_sides) + modifier
            total += roll_result

        if use_morph_die:
            total += roll_morph_die(starting_die=starting_morph_die)
        total += modifier

        results_distribution[total] += 1
        if total >= dc:
            successes += 1

    success_rate = successes / trials
    return success_rate, dict(sorted(results_distribution.items()))

if __name__ == "__main__":
    #Example: 1d4 + 1 against DC 5
    dice_config = [Die.D4] #1d4
    modifier = 0
    dc = 5
    trials = 100000

    success_rate, distribution = simulate_rolls(
        dice=dice_config,
        modifier=modifier,
        dc=dc,
        trials=trials,
        use_morph_die=False,
        starting_morph_die=Die.D4 #start morph die at 4
    ) #Enables the morph die

    print(f"Success Rate: {success_rate:.2%}")
    print("Roll Totals Distribution:")
    for total, count in distribution.items():
        print(f"{total}: {count}")


