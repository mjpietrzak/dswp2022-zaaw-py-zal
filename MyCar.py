from math import exp

class Car:
    def __init__(self, make, model, year, milage, price):
        self.make = make
        self.model = model
        self.year = year
        self.milage = milage
        self.price = price
    
    
    @property
    def milage(self):
        return self.__milage

    @milage.setter
    def milage(self, value):
        assert value >= 0
        self.__milage = value
        
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        assert value >= 0
        self.__price = value
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - {self.milage} km, {self.price} PLN"
    
    def __repr__(self):
        return self.__str__()
    
    def drive(self, dist):
        assert dist >= 0
        self.milage += dist
    
    def current_value(self):
        salvage_price = 500
        
        y = 1/exp(1-(self.year-2013)/(2023-2013))
        
        m = (1 - (self.milage/1e6)**.7)
        if m < 0:
            m = 0
            
        return self.price * m * y + salvage_price

    def calculate_deprecation(self):
        return self.price - self.current_value()


if __name__ == "__main__":
    vw_golf_2010 = Car("Volkswagen", "Golf", 1990, 512345, 71000)  # initial price
    citroen_c5 = Car("Citroen", "C5", 2011, 222000, 123000)
    audi_a8 = Car("Audi", "A8", 2020, 72000, 500000)
    
    for c in (vw_golf_2010, citroen_c5, audi_a8):
        print(f"\n{c}")
        print(f"Current price: {c.current_value():.0f} PLN, deprecation: {c.calculate_deprecation():.0f} PLN")
        c.drive(2e4)
        print(f"Price after another 20 000 km: {c.current_value():.0f} PLN")
        
