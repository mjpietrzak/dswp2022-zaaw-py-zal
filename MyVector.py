import warnings


class Vector2D:
    def __init__(self, x, y=None):
        if y is None:
            x, y = x
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, (list, tuple)):
            return Vector2D(self.x + other[0], self.y + other[1])
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __str__(self):
        return f"[{self.x:.3g}, {self.y:.3g}]"
    
    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    v1 = Vector2D(4, 5)
    
    v2 = Vector2D((-1, -0.4))
    
    v3 = (-2, 1)
    
    v4 = Vector2D(v3)
    
    print(v1, v2, v1 + v2)
    print(v2, v1, v2 + v1)
    
    print(v1, v3, v1 + v3)
    print(v3, v1, v3 + v1)
    
    print(v3, v4, v3 + v4)
    
