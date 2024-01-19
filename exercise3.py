class Location:
    def __init__(self, name, code):
        self.name, self.code = name, code

class Product:
    def __init__(self, name, code):
        self.name, self.code, self.stock_at_locations = name, code, {}

    def display_info(self):
        print(f"\nProduct: {self.name} (Code: {self.code}), Stock at Locations: {self.stock_at_locations}")

class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location, self.to_location, self.product, self.quantity = from_location, to_location, product, quantity

    @staticmethod
    def movements_by_product(product):
        return [movement for movement in movements if movement.product == product]

# Create Location objects
location1 = Location("Location1", "L001")
location2 = Location("Location2", "L002")
location3 = Location("Location3", "L003")
location4 = Location("Location4", "L004")

# Create Product objects
product1 = Product("Product1", "P001")
product2 = Product("Product2", "P002")
product3 = Product("Product3", "P003")
product4 = Product("Product4", "P004")
product5 = Product("Product5", "P005")

# Add new members inside the product “stock_at_locations” with initial stock at each location
for product in [product1, product2, product3, product4, product5]:
    product.stock_at_locations = {location1: 10, location2: 5, location3: 7, location4: 3}

# Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve.
movements = [
    Movement(location1, location2, product1, 10),
    Movement(location2, location3, product1, 5),
    Movement(location3, location4, product1, 7),
    Movement(location4, location1, product1, 3),
    Movement(location1, location2, product2, 8),
    Movement(location2, location3, product2, 6),
    Movement(location3, location4, product2, 2),
]

# Manage exceptions if product stock goes negative
for movement in movements:
    if movement.product.stock_at_locations.get(movement.from_location, 0) - movement.quantity < 0:
        print(f"Error: Insufficient stock of {movement.product.name} at {movement.from_location.name}")
    else:
        movement.product.stock_at_locations[movement.from_location] -= movement.quantity
        movement.product.stock_at_locations[movement.to_location] = movement.product.stock_at_locations.get(movement.to_location, 0) + movement.quantity

# Display movements of each product
for product in [product1, product2, product3, product4, product5]:
    print(f"\nMovements for {product.name} (Code: {product.code}):")
    for movement in Movement.movements_by_product(product):
        print(f"From: {movement.from_location.name} To: {movement.to_location.name}, Quantity: {movement.quantity}")

# Display product details with its stock at various locations
def display_product_list_by_location():
    locations = [location1, location2, location3, location4]

    for location in locations:
        print(f"\nLocation: {location.name}")
        for product in [product1, product2, product3, product4, product5]:
            stock = product.stock_at_locations.get(location, 0)
            print(f"Product: {product.name} (Code: {product.code}), Stock: {stock} units")

# Display product list by location
display_product_list_by_location()
