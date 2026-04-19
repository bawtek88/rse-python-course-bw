import pint

si = pint.UnitRegistry()

def calculate_current_velocity(V0, a, t) -> pint.Quantity:
    """Calculate the velocity of an object at time t, using the formula $$v = v_0 + at$$.

    Parameters
    ----------
    V0 : float or pint.Quantity 
        Initial velocity of the object ($v_0$) at time $t = 0$, by default in meters per second (m/s).
    a : float or pint.Quantity
        Constant acceleration of the object, by default in meters per second squared (m/s^2).
    t : float or pint.Quantity
        Time at which we want to calculate the velocity, nonnegative, by default in seconds (s).
    
    Returns
    -------
    pint.Quantity
        Velocity at time $t$, in meters per second (m/s).

    Raises
    ------
    ValueError
        If time `t` is negative.
    pint.errors.DimensionalityError
        If any input has incompatible units
    """
    
    
    if not isinstance(V0, si.Quantity):
        V0 = V0 * si.m / si.s
    V0 = V0.to(si.m / si.s)

    if not isinstance(a, si.Quantity):
        a = a * si.m / (si.s**2)
    a  = a.to(si.m / si.s**2)

    if not isinstance(t, si.Quantity):
        t = t * si.s
    t  = t.to(si.s)

    if t.magnitude < 0:
        raise ValueError("Time cannot be a negative number")
    
    return V0 + a * t
