import pint
import pytest
import kinematicsbw

si = kinematicsbw._si

def test_calculate_current_velocity_correctness():
    value = kinematicsbw.calculate_current_velocity(3, 3, 3)

    assert value.units == si.m / si.s
    assert value.magnitude == pytest.approx(12.0)

def test_calculate_current_velocity_correct_units():
    value = kinematicsbw.calculate_current_velocity(
        36 * si.km / si.hour,
        400 * si.cm / si.s**2,
        1 * si.s,
    )

    assert value.units == si.m / si.s
    assert value.magnitude == pytest.approx(14.0)

def test_calculate_current_velocity_invalid_time():
    with pytest.raises(ValueError, match = "Time cannot be a negative number"):
        kinematicsbw.calculate_current_velocity(1, 2, -1)

def test_calculate_current_velocity_incompatible_units():
    with pytest.raises(pint.errors.DimensionalityError):
        kinematicsbw.calculate_current_velocity(
            3 * si.kg,
            4 * si.m / si.s**2,
            5 * si.s,
        )
