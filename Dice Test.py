import random
from collections import defaultdict

def simulate_rolls(dice, modifier=0, dc=10, trials=10000):
    """
    Simulates a number of dice rolls to determine success rate

    Parameters:
    -dice: potential values that can be rolled, representing different die (e.g., [4] for 1d4, [6] for 1d6, etc)
    -modifier: static bonus to the roll (default 0, could be 1, 2, 3, etc)
    -dc: difficulty class to meet or beat
    -trials: simulations ran
    """

    
