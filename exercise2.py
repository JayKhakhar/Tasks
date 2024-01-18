class VehicleCategory:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_info(self):
        category_chain = self.get_category_chain()
        print(f"Category: {category_chain}")
        print(f"Code: {self.code}")
        print("\nProduct Details:")
        for product in self.products:
            product.display_info()
        
    def get_category_chain(self):
        if self.parent:
            return f"{self.parent.get_category_chain()} > {self.name}"
        return self.name

class VehicleProduct:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Code: {self.code}\n")

vehicle_category = VehicleCategory(name="Vehicle", code="V001")
car_category = VehicleCategory(name="Car", code="C001", parent=vehicle_category)
bike_category = VehicleCategory(name="Bike", code="B001", parent=vehicle_category)
diesel_car_category = VehicleCategory(name="Diesel Car", code="DC001", parent=car_category)
petrol_car_category = VehicleCategory(name="Petrol Car", code="PC001", parent=car_category)

products_vehicle = [VehicleProduct("Vehicle Product", f"VP00{i}") for i in range(3)]
products_car = [VehicleProduct("Car Product", f"CP00{i}") for i in range(3)]
products_bike = [VehicleProduct("Bike Product", f"BP00{i}") for i in range(3)]
products_diesel_car = [VehicleProduct("Diesel Car Product", f"DCP00{i}") for i in range(3)]
products_petrol_car = [VehicleProduct("Petrol Car Product", f"PCP00{i}") for i in range(3)]

for product in products_vehicle:
    vehicle_category.add_product(product)

for product in products_car:
    car_category.add_product(product)

for product in products_bike:
    bike_category.add_product(product)

for product in products_diesel_car:
    diesel_car_category.add_product(product)

for product in products_petrol_car:
    petrol_car_category.add_product(product)

for category in [vehicle_category, car_category, bike_category, diesel_car_category, petrol_car_category]:
    category.display_info()
