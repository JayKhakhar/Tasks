class Category:
    def __init__(self, name, code, parent=None):
        self.name, self.code, self.parent = name, code, parent
        self.display_name = ""
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def generate_display_name(self):
        if self.parent:
            self.parent.generate_display_name()
            self.display_name = f"{self.parent.display_name} > {self.name}"
        else:
            self.display_name = self.name

    def add_products_recursive(self, products):
        for product in products:
            self.add_product(product)

        for child_category in self.products:
            if isinstance(child_category, Category):
                child_category.add_products_recursive(products)

    def display_info(self):
        print(f"\nCategory: {self.display_name}\nCode: {self.code}\nProducts:")
        if not self.products:
            print("No products")
        else:
            for product in self.products:
                product.display_info()

    def get_category_chain(self):
        return [self.display_name] + (self.parent.get_category_chain() if self.parent else [])


class Product:
    def __init__(self, name, code):
        self.name, self.code = name, code

    def display_info(self):
        print(f"  Product: {self.name}\n  Code: {self.code}")


# Creating category objects
vehicle_category = Category("Vehicle", "V001")
car_category = Category("Car", "C001", vehicle_category)
petrol_category = Category("Petrol", "P001", car_category)
diesel_category = Category("Diesel", "D001", car_category)
bike_category = Category("Bike", "B001", vehicle_category)

# Generating display names for categories
for category in [vehicle_category, car_category, petrol_category, diesel_category, bike_category]:
    category.generate_display_name()

# Creating static product objects
products_vehicle = [Product(f"Product{num}", f"VP{num + 1:03}") for num in range(3)]
products_car = [Product(f"Product{num}", f"CP{num + 1:03}") for num in range(3)]
products_petrol = [Product(f"Product{num}", f"PP{num + 1:03}") for num in range(3)]
products_diesel = [Product(f"Product{num}", f"DP{num + 1:03}") for num in range(3)]
products_bike = [Product(f"Product{num}", f"BP{num + 1:03}") for num in range(3)]

# Adding static products to respective categories using recursion
vehicle_category.add_products_recursive(products_vehicle)
car_category.add_products_recursive(products_car)
petrol_category.add_products_recursive(products_petrol)
diesel_category.add_products_recursive(products_diesel)
bike_category.add_products_recursive(products_bike)

# Displaying product list by category (group by category, order by category name)
categories = [vehicle_category, car_category, petrol_category, diesel_category, bike_category]
categories.sort(key=lambda x: x.display_name)

for category in categories:
    category.display_info()
