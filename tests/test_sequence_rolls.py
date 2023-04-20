import pytest
from random import seed, randint
from unittest.mock import patch
from dnd_roller.dice import sequence_rolls, roll


@patch("dnd_roller.dice.dice_roll")
def test_dice_roll_is_called_in_sequence_rolls(dice_roll_mock):
    sequence_rolls(sequence="2d4")
    dice_roll_mock.assert_called()
    dice_roll_mock.assert_called_with(2, 4)


def unfair_dice(sequence, rnd_seed: int) -> dict[int, list[int]]:
    """generates a fixed list of t rolls for each die in sequence."""

    seed(rnd_seed)  # this does the trick!
    return {d: [randint(1, d) for _ in range(t)] for t, d in sequence}


def test_roll_is_repeatable():
    # FIX the random seed
    rnd_seed = 123456
    unfair_rolls = unfair_dice(((2, 4),), rnd_seed=rnd_seed)
    seed(rnd_seed)
    assert roll(4) == unfair_rolls[4][0]
    assert roll(4) == unfair_rolls[4][1]


def test_sequence_rolls_with():
    sequence = "2d4, 6d6, 4d8"
    rnd_seed = 4567

    unfair_rolls = unfair_dice(((2, 4), (6, 6), (4, 8)), rnd_seed=rnd_seed)
    seed(rnd_seed)

    rolls = sequence_rolls(sequence=sequence)
    assert "2d4" in rolls
    assert len(rolls["2d4"]) == 2
    assert all(r == unfr for r, unfr in zip(rolls["2d4"], unfair_rolls[4]))

    assert "4d8" in rolls
    assert len(rolls["4d8"]) == 4
    assert all(r == unfr for r, unfr in zip(rolls["4d8"], unfair_rolls[8]))

    assert "6d6" in rolls
    assert len(rolls["6d6"]) == 6
    assert all(r == unfr for r, unfr in zip(rolls["6d6"], unfair_rolls[6]))
