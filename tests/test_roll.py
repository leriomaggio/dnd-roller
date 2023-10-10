import pytest
from dnd_roller import roll, SUPPORTED_DICE


@pytest.mark.parametrize("dface", SUPPORTED_DICE[:-1])
def test_roll_die_return_a_valid_number(dface):
    assert roll(dface) in range(1, dface + 1)


def test_roll_d100():
    assert roll(100) in range(1, 101)
    assert roll(100) % 10 == 0


def test_roll_with_nan_string_will_raise_exception():
    with pytest.raises(ValueError):
        roll("not a die")


@pytest.mark.parametrize("dface", SUPPORTED_DICE[:-1])
def test_roll_with_no_string_will_still_work_as_expected(dface):
    assert roll(str(dface)) in range(1, dface + 1)


def test_roll_with_unsupported_dice_will_raise_exception():
    with pytest.raises(ValueError):
        roll(45)


@pytest.mark.parametrize("dface", [-4, 2.3, 11.8])
def test_roll_with_negative_or_float_no_will_raise_exception(dface):
    with pytest.raises(ValueError):
        roll(dface)
