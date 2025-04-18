import math

def circle_area(radius: float) -> float:

    if radius <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * (radius ** 2)

def triangle_area(a: float, b: float, c: float) -> float:
    
    if not all(x > 0 for x in (a, b, c)):
        raise ValueError("All sides must be positive")
    
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Invalid triangle sides")
    
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    sides = sorted([a, b, c])
    is_right = math.isclose(
        sides[0]**2 + sides[1]**2, 
        sides[2]**2, 
        rel_tol=1e-9
    )
    
    return (area, is_right)
