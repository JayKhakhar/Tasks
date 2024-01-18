class Category:
    def __init__(self, name, code, parent=None):
        self.name, self.code, self.parent = name, code, parent
        self.display_name = ""
        self.products = []

        if self.parent:
            self.display_name = f"{self.parent.display_name} > {self.name}"
        else:
            self.display_name = self.name

    def add_product(self, product):
        self.products.append(product)

    def display_info(self):
        print(f"\nCategory: {self.display_name}\nCode: {self.code}\nProducts:")
        if not self.products:
            print("No products")
        else:
            for product in self.products:
                product.display_info()

    def add_products_recursive(self, products):
        def add_to_category(category, products):
            for product in products:
                category.add_product(product)

            for child_category in category.products:
                if isinstance(child_category, Category):
                    add_to_category(child_category, products)

        add_to_category(self, products)

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

# Creating static product objects
products_vehicle = [Product(f"Product{num}", f"VP{num + 1:03}") for num in range(3)]
products_car = [Product(f"Product{num}", f"CP{num + 1:03}") for num in range(3)]
products_petrol = [Product(f"Product{num}", f"PP{num + 1:03}") for num in range(3)]
products_diesel = [Product(f"Product{num}", f"DP{num + 1:03}") for num in range(3)]
products_bike = [Product(f"Product{num}", f"BP{num + 1:03}") for num in range(3)]

# List of tuples containing a category and its corresponding products
category_product_tuples = [
    (vehicle_category, products_vehicle),
    (car_category, products_car),
    (petrol_category, products_petrol),
    (diesel_category, products_diesel),
    (bike_category, products_bike),
]

# Adding static products to respective categories using recursion
for category, products in category_product_tuples:
    category.add_products_recursive(products)

# Displaying product list by category (group by category, order by category name)
categories = [vehicle_category, car_category, petrol_category, diesel_category, bike_category]
categories.sort(key=lambda x: x.display_name)

for category in categories:
    category.display_info()
