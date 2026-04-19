import pint

_si = pint.UnitRegistry()

def calculate_current_velocity(V0, a, t) -> pint.Quantity:
    """Calculate the velocity of an object at time `t`.  
    Formula: `V = V0 + a * t`.  

    Parameters
    ----------
    V0 : float or pint.Quantity    
        Initial velocity of an object (velocity at time `t=0`), by default in meters per second (m/s).
    a : float or pint.Quantity    
        Acceleration of an object, by default in meters per second squared (m/s^2).  
    t : float or pint.Quantity    
        Time at which we want to calculate the velocity, nonnegative, by default in seconds (s).  

    Returns
    -------
    pint.Quantity    
        Velocity at time `t`, in meters per second (m/s).

    Raises
    ------
    ValueError    
        If time `t` is negative.  
    pint.errors.DimensionalityError    
        If input has incompatible units.  
    """
        
    if not isinstance(V0, _si.Quantity):
        V0 = V0 * _si.m / _si.s
    V0 = V0.to(_si.m / _si.s)

    if not isinstance(a, _si.Quantity):
        a = a * _si.m / (_si.s**2)
    a  = a.to(_si.m / _si.s**2)

    if not isinstance(t, _si.Quantity):
        t = t * _si.s
    t  = t.to(_si.s)

    if t.magnitude < 0:
        raise ValueError("Time cannot be a negative number")
    
    return V0 + a * t
