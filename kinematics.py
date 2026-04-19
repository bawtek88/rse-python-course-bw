import pint

si = pint.UnitRegistry()

def calculate_current_velocity(V0, a, t) -> pint.Quantity:
    """
    Calculate the velocity of an object at time `t`.
    
    **Formula:** `V = V0 + a * t`
    
    **Parameters:**

    * **V0** (float | pint.Quantity): Initial velocity of the object `V0` at time `t = 0`.
        Default: meters per second (m/s).
    * **a** (float | pint.Quantity): Constant acceleration of the object.
        Default: meters per second squared (m/s^2).
    * **t** (float | pint.Quantity): Time at which we want to calculate the velocity, nonnegative.
        Default: seconds (s).
    
    **Returns:**
    
    * **pint.Quantity**: Velocity at time `t`, in meters per second (m/s).
  
    **Raises:**
    
    * **ValueError**: If time `t` is negative.
    * **pint.errors.DimensionalityError**: If any input has incompatible units
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
