import pint

si = pint.UnitRegistry()

def calculate_current_velocity(V0, a, t) -> pint.Quantity:
    """Calculate the velocity of an object at time t.

    Parameters
    ----------
    V0 : float or pint.Quantity 
        initial velocity of an object(velocity at time t = 0), by default in meters per second (m/s)
    a : float or pint.Quantity
        acceleration of an object, by default in meters per seconds squared (m/s^2)
    t : float or pint.Quantity
        time at which we want to calculate the velocity,nonnegative, by default in seconds (s)
    
    Returns
    -------
    pint.Quantity
        velocity at time t, in meters per second (m/s)

    Raises
    ------
    ValueError
        if time t is negative
    pint.errors.DimensionalityError
        if input has incompatible units
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
