import pytest
from unittest.mock import patch
from dnd_roller.dice import dice_roll


@pytest.mark.parametrize("throws, sides", [(2, 4), (1, 6), (4, 8), (1, 10)])
def test_dice_rolls(throws, sides):
    rolls = dice_roll(throws=throws, sides=sides)
    assert len(rolls) == throws
    assert all([r in range(1, sides + 1) for r in rolls])


@patch("dnd_roller.dice.roll")
def test_dice_roll_calls_roll(roll_mock):
    dice_roll(throws=2, sides=4)
    roll_mock.assert_called()
    roll_mock.assert_called_with(d=4)