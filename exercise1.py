class Category:
    def __init__(self, name, code, no_of_products):
        self.name = name
        self.code = code
        self.no_of_products = no_of_products


class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price


def find_min_price(products):
    if not products:
        return None
    min_price_product = products[0]
    for product in products:
        if product.price < min_price_product.price:
            min_price_product = product
    return min_price_product


def sort_by_price(products):
    sorted_products = []
    while products:
        min_price_product = find_min_price(products)
        sorted_products.append(min_price_product)
        products.remove(min_price_product)
    return sorted_products


def search_product_by_code(products, search_code):
    for product in products:
        if product.code == search_code:
            return product
    return None



categories = []
num_categories = int(input("Enter the number of categories: "))
for i in range(1, num_categories + 1):
    name = input(f"Enter the name of category {i}: ")
    code = input(f"Enter the code of category {i}: ")
    no_of_products = int(input(f"Enter the number of products in category {i}: "))
    categories.append(Category(name, code, no_of_products))


products = []
for category in categories:
    for i in range(1, category.no_of_products + 1):
        name = input(f"Enter the name of product {i} in category {category.name}: ")
        code = input(f"Enter the code of product {i} in category {category.name}: ")
        price = float(input(f"Enter the price of product {i} in category {category.name}: "))
        products.append(Product(name, code, category.name, price))


for category in categories:
    print(f"Category: {category.name}")
    print(f"Code: {category.code}")
    print(f"Number of Products: {category.no_of_products}")


# Sorting products based on price (Low to High) without using sort or sorted
print("Products sorted by price (Low to High):")
sorted_low_to_high = sort_by_price(products.copy())
for product in sorted_low_to_high:
    print(f"Name: {product.name}")
    print(f"Code: {product.code}")
    print(f"Category: {product.category}")
    print(f"Price: ${product.price}")



print("Products sorted by price (High to Low):")
sorted_high_to_low = sort_by_price(products.copy())
sorted_high_to_low.reverse()  # Reverse the list for High to Low
for product in sorted_high_to_low:
    print(f"Name: {product.name}")
    print(f"Code: {product.code}")
    print(f"Category: {product.category}")
    print(f"Price: ${product.price}")



search_code = input("Enter the product code to search: ")
found_product = search_product_by_code(products, search_code)

if found_product:
    print(f"Product with code {search_code} found:")
    print(f"Name: {found_product.name}")
    print(f"Category: {found_product.category}")
    print(f"Price: ${found_product.price}")
else:
    print(f"Product with code {search_code} not found.")
