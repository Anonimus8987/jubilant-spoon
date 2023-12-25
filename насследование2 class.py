class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def display_info(self):
        super().display_info()
        print(f"Model: {self.model} (Car)")


class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Type: {self.type} (Motorcycle)")


car_obj = Car("Toyota", 2022, "Camry")
motorcycle_obj = Motorcycle("Harley-Davidson", 2021, "Cruiser")

car_obj.display_info()
print("\n")
motorcycle_obj.display_info()