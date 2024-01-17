class Category:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.display_name = self.generate_display_name()
        self.products = [self.create_product() for i in range(3)]

    def generate_display_name(self):
        if self.parent is None:
            return self.name
        else:
            return f"{self.parent.generate_display_name()} > {self.name}"

    def create_product(self):
        product_name = input(f"Enter the product name for {self.name}: ")
        product_code = input(f"Enter the product code for {self.name}: ")
        product_price = float(input(f"Enter the product price for {self.name}: "))
        return Product(product_name, product_code, product_price)

class Product:
    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price

vehicle = Category("Vehicle", "V001")
car = Category("Car", "C005", parent=vehicle)
petrol = Category("Petrol", "P004", parent=car)

category1 = Category("Category1", "C001", parent=vehicle)
category2 = Category("Category2", "C002", parent=category1)
category3 = Category("Category3", "C003", parent=category1)
category4 = Category("Category4", "C004", parent=category3)
category5 = Category("Category5", "C005", parent=category3)

def display_category(category):
    print(f"\nCategory: {category.name}")
    print(f"Code: {category.code}")
    print(f"Display Name: {category.display_name}")
    print("Product Details:")
    for product in category.products:
        print(f"  Product: {product.name}")
        print(f"    Code: {product.code}")
        print(f"    Price: ${product.price}")

categories = [vehicle, car, petrol, category1, category2, category3, category4, category5]
categories.sort(key=lambda x: x.display_name)

for category in categories:
    display_category(category)
