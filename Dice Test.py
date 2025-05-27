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

def simulate_rolls(dice, modifier=0, dc=10, trials=10000):
    """
    Simulates a number of dice rolls to determine success rate

    Parameters:
    -dice: potential values that can be rolled, representing different die (e.g., [4] for 1d4, [6] for 1d6, etc)
    -modifier: static bonus to the roll (default 0, could be 1, 2, 3, etc)
    -dc: difficulty class to meet or beat
    -trials: simulations ran
    """

    successes = 0
    results_distribution = defaultdict(int)

    for _ in range(trials):
        total = sum(roll_exploding_die(s) for s in dice) + modifier
        if total >= dc:
            successes += 1

    for _ in range(trials):
        total = sum(roll_exploding_die(s) for s in dice) + modifier
        results_distribution[total] += 1
        if total >= dc:
            successes += 1

    success_rate = successes / trials
    return success_rate, dict(sorted(results_distribution.items()))

if __name__ == "__main__":
    #Example: 1d4 + 1 against DC 5
    dice_config = [4] #1d4
    modifier = 1
    dc = 5
    trials = 10000

    success_rate, distribution = simulate_rolls(dice=dice_config, modifier=modifier, dc=dc, trials=trials)

    print(f"Success Rate: {success_rate:.2%}")
    print("Roll Totals Distribution:")
    for total, count in distribution.items():
        print(f"{total}: {count}")


