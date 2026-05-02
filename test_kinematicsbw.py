import pint
import pytest
import kinematics

si = kinematics._si

def test_calculate_current_velocity_correctness():
    value = kinematics.calculate_current_velocity(3, 3, 3)

    assert value.units == si.m / si.s
    assert value.magnitude == pytest.approx(12.0)

def test_calculate_current_velocity_correct_units():
    value = kinematics.calculate_current_velocity(
        36 * si.km / si.h,
        400 * si.cm / si.s**2,
        1 * si.s,
    )

    assert value.units == si.m / si.s
    assert value.magnitude == pytest.approx(14.0)

def test_calculate_current_velocity_invalid_time():
    with pytest.raises(ValueError, match = "Time cannot be a negative number"):
        kinematics.calculate_current_velocity(1, 2, -1)

def test_calculate_current_velocity_incompatible_units():
    with pytest.raises(pint.errors.DimensionalityError):
        kinematics.calculate_current_velocity(
            3 * si.kg,
            4 * si.m / si.s**2,
            5 * si.s,
        )
