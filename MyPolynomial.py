from itertools import zip_longest


class Polynomial:
    def __init__(self, p, *args):
        if len(args) > 0:
            p = [p] + list(args)
        elif isinstance(p, (list, tuple)):
            p = list(p)
        else:
            p = [p]
        self.params = p
    
    def __getitem__(self, item):
        return self.params[item]
    
    def __setitem__(self, key, value):
        self.params[key] = value
    
    def __add__(self, other):
        p = [p1 + p2 for p1, p2 in zip_longest(self, other, fillvalue = 0)]
        return Polynomial(*p)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __str__(self):
        return f"{self.params}"
    
    def __repr__(self):
        return self.__str__()
    
    def eval(self, x):
        return sum([p*x**i for i, p in enumerate(self.params)])

    def __call__(self, x):
        return self.eval(x)


if __name__ == "__main__":
    poly0 = Polynomial(5)
    poly4 = Polynomial(0, 4, 5, 0, 7)
    
    poly2 = Polynomial((-1, -0.4))
    
    poly3 = (-2, 1, 1)
    
    poly3_ = Polynomial(poly3)
    
    print(poly4, poly2, poly4 + poly2, )
    print(poly2, poly4, poly2 + poly4)
    
    print(poly4, poly3, poly4 + poly3)
    print(poly3, poly4, poly3 + poly4)
    
    print(poly3, poly4, poly3 + poly4)
    
    print()
    for x in (-2, -1, 0, 1, 2):
        print(f"poly1({x}) = {poly4.eval(x)}")
    
    print()
    for x in (-2, -1, 0, 1, 2):
        print(f"poly0({x}) = {poly0(x)}")
