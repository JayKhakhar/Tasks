class Category:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.products = []
        self.no_of_products = 0

    def add_product(self, product):
        self.products.append(product)
        self.no_of_products += 1

    def display_info(self):
        print(f"Category: {self.name}")
        print(f"Code: {self.code}")
        print(f"Number of Products: {self.no_of_products}\n")

    def search_product_by_code(self, code):
        for product in self.products:
            if product.code == code:
                return product
        return None


class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        category.add_product(self)

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Code: {self.code}")
        print(f"Category: {self.category.name}")
        print(f"Price: ${self.price}")

def bubble_sort(products, reverse=False):
    n = len(products)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (products[j].price < products[j + 1].price) if reverse else (products[j].price > products[j + 1].price):
                products[j], products[j + 1] = products[j + 1], products[j]


electronics_category = Category(name="Electronics", code="E001")
clothing_category = Category(name="Clothing", code="C002")
books_category = Category(name="Books", code="B003")

products = [
    Product(name="Laptop", code="P001", category=electronics_category, price=1200),
    Product(name="T-shirt", code="P002", category=clothing_category, price=25),
    Product(name="Smartphone", code="P003", category=electronics_category, price=800),
    Product(name="Jeans", code="P004", category=clothing_category, price=40),
    Product(name="Book1", code="P005", category=books_category, price=15),
    Product(name="Book2", code="P006", category=books_category, price=20),
    Product(name="Camera", code="P007", category=electronics_category, price=300),
    Product(name="Sweater", code="P008", category=clothing_category, price=30),
    Product(name="Tablet", code="P009", category=electronics_category, price=150),
    Product(name="Hat", code="P010", category=clothing_category, price=10),
]

for category in [electronics_category, clothing_category, books_category]:
    category.display_info()

bubble_sort(products, reverse=True)
print("Products Sorted by Price (High to Low):")
for product in products:
    product.display_info()

bubble_sort(products)
print("Products Sorted by Price (Low to High):")
for product in products:
    product.display_info()

search_code = input("Enter the product code to search: ")

found_product = None
for category in [electronics_category, clothing_category, books_category]:
    found_product = category.search_product_by_code(search_code)
    if found_product:
        break

if found_product:
    print("\nProduct Found:")
    found_product.display_info()
else:
    print("\nProduct not found.")
