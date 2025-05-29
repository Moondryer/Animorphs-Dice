import random
from collections import defaultdict

def roll_exploding_die(sides):
    """Rolls an exploding die. If the max value is rolled, it rolls again and adds the result."""
    total = 0
    roll = sides
    while roll == sides:
        roll = random.randint(1, sides)
        total += roll
    return total

def roll_morph_die(starting_die=4):
    """
    Rolls a morph die, progressing up the chain on a max roll.
    Terminates if a natural 20 is rolled on a d20.
    """
    die_chain = [4, 6, 8, 10, 12, 20]

    if starting_die not in die_chain:
        raise ValueError(f"Starting die must be one of: {die_chain}")

    index = die_chain.index(starting_die)
    total = 0

    while index < len(die_chain):
        sides = die_chain[index]
        roll = random.randint(1, sides)
        total += roll

        if sides == 20 and roll == 20:
            break  # terminate the morphing sequence if 20 on d20
        elif roll == sides:
            index += 1  # move to next bigger die
        else:
            break  # no explosion, end morph sequence

    return total

def simulate_rolls(dice, modifier=0, dc=10, trials=10000, use_morph_die=False, starting_morph_die=4):
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
        total = sum(roll_exploding_die(s) for s in dice) + modifier
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
    dice_config = [4] #1d4
    modifier = 0
    dc = 7
    trials = 10000

    success_rate, distribution = simulate_rolls(
        dice=dice_config,
        modifier=modifier,
        dc=dc,
        trials=trials,
        use_morph_die=True,
        starting_morph_die=8 #start morph die at 4
    ) #Enables the morph die

    print(f"Success Rate: {success_rate:.2%}")
    print("Roll Totals Distribution:")
    for total, count in distribution.items():
        print(f"{total}: {count}")


