class Location:
    def __init__(self, name, code):
        self.name, self.code = name, code

class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location, self.to_location, self.product, self.quantity = from_location, to_location, product, quantity

    def process_movement(self):
        if self.product.stock_at_locations.get(self.from_location, 0) - self.quantity < 0:
            print(f"Error: Insufficient stock of {self.product.name} at {self.from_location.name}")
        else:
            self.product.stock_at_locations[self.from_location] -= self.quantity
            self.product.stock_at_locations[self.to_location] = self.product.stock_at_locations.get(self.to_location, 0) + self.quantity
            self.product.movements.append(self)

class Product:
    def __init__(self, name, code):
        self.name, self.code = name, code
        self.stock_at_locations = {}
        self.movements = []

    def display_stock_at_locations(self):
        print(f"\nStock at various locations for {self.name} (Code: {self.code}):")
        for location, stock in self.stock_at_locations.items():
            print(f"  {location.name}: {stock} units")

    def display_movements(self):
        print(f"\nMovements for {self.name} (Code: {self.code}):")
        if not self.movements:
            print("  No movement")
        else:
            for movement in self.movements:
                print(f"  Moved {movement.quantity} units from {movement.from_location.name} to {movement.to_location.name}")


# Creating location objects
location1 = Location("Location1", "L001")
location2 = Location("Location2", "L002")
location3 = Location("Location3", "L003")
location4 = Location("Location4", "L004")

# Creating product objects
product1 = Product("Product1", "P001")
product2 = Product("Product2", "P002")
product3 = Product("Product3", "P003")
product4 = Product("Product4", "P004")
product5 = Product("Product5", "P005")

# Initializing stock at locations for products
product1.stock_at_locations = {location1: 7}
product2.stock_at_locations = {location1: 6}
product3.stock_at_locations = {location1: 6}
product4.stock_at_locations = {location2: 4}
product5.stock_at_locations = {location3: 2}

# Creating movement objects
movement1 = Movement(location1, location2, product3, 3)

# Processing movement
movement1.process_movement()

# Displaying initial stock and movements
for product in [product1, product2, product3, product4, product5]:
    product.display_stock_at_locations()
    product.display_movements()

# Displaying product list by location (group by location)
location_product_dict = {}
for product in [product1, product2, product3, product4, product5]:
    for location, stock in product.stock_at_locations.items():
        if location not in location_product_dict:
            location_product_dict[location] = []
        location_product_dict[location].append((product.name, stock))

print("\nProduct list by location (group by location):")
for location, products in location_product_dict.items():
    print(f"{location.name}: {', '.join([f'{product} ({stock} units)' for product, stock in products])}")
