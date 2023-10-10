from random import randint
from tabulate import tabulate

SUPPORTED_DICE = (4, 6, 8, 10, 12, 20, 100)
HEADERS = ["dice", "rolls", "sum"]


def roll(d: int, verbose: bool = False) -> int:
    """Roll a single die choosing one of d4, d6, d8, d10, d12, d20, d100"""
    try:
        d = int(d)
    except ValueError:
        raise ValueError(f"'{d}' is not an appropriate number of faces.")
    else:
        if d not in SUPPORTED_DICE:
            raise ValueError("Unsupported Game die for D&D")
        r = randint(1, d) if d != 100 else (randint(1, 10) * 10)

        if verbose:
            print("You rolled ", r)
        return r


def dice_roll(throws: int, sides: int) -> list[int]:
    """Rolls a single die with given `sides` a `throws` number of times"""
    return [roll(d=sides) for _ in range(throws)]


def sequence_rolls(sequence: str, verbose: bool = True) -> str:
    """Generating a tabular summary of a sequence of dice rolls passed in input.
    Each dice roll are comma separated, and defined in the form of
    `throwsdface`, e.g. 2d12."""
    rolls_in_sequence = {
        roll: dice_roll(*tuple(map(int, roll.split("d"))))
        for roll in map(str.strip, sequence.split(","))
    }

    if verbose:
        table = [(seq, rolls, sum(rolls)) for seq, rolls in rolls_in_sequence.items()]
        print(tabulate(table, headers=HEADERS, tablefmt="fancy_grid"))

    return rolls_in_sequence
