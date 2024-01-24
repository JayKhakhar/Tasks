import re
from datetime import datetime, timedelta

class Customer:
    def __init__(self, name, email, phone, city, state, country, company=None, type="contact"):
        self.name = self.validate_name(name)
        self.email = self.validate_email(email)
        self.phone = self.validate_phone(phone)
        self.city = self.validate_city(city)
        self.state = self.validate_state(state)
        self.country = self.validate_country(country)
        self.company = self.validate_company(company)
        self.type = self.validate_type(type)

    def validate_name(self, name):
        if any(char.isdigit() for char in name):
            raise ValueError("Name cannot contain numbers.")
        return name

    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        return email

    def validate_phone(self, phone):
        if not (phone.isdigit() and len(phone) == 10):
            raise ValueError("Invalid phone number format. Please enter a 10-digit number.")
        return phone

    def validate_city(self, city):
        if any(char.isdigit() for char in city):
            raise ValueError("City name cannot contain numbers.")
        return city

    def validate_state(self, state):
        if any(char.isdigit() for char in state):
            raise ValueError("State name cannot contain numbers.")
        return state

    def validate_country(self, country):
        if any(char.isdigit() for char in country):
            raise ValueError("Country name cannot contain numbers.")
        return country

    def validate_company(self, company):
        if company and not isinstance(company, Customer):
            raise ValueError("\"Company\" must be a Customer object.")
        return company

    def validate_type(self, type):
        valid_types = ["company", "contact", "billing", "shipping"]
        if type not in valid_types:
            raise ValueError("Invalid customer type. Allowed types are: company, contact, billing, shipping.")
        return type

    def display_customer_info(self):
        print(f"Customer Information: {self.name}, {self.email}, {self.phone}, {self.city}, {self.state}, {self.country}, {self.type}")

class OrderLine:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.calculate_subtotal()

    def calculate_subtotal(self):
        return self.quantity * self.price if self.quantity is not None and self.price is not None else None

    def display_order_line_info(self):
        return f"Order Line Information: {self.product}, {self.quantity}, {self.price}, {self.subtotal}"

class Order:
    def __init__(self, number, date, company, billing, shipping, order_lines):
        self.number = number
        self.date = self.validate_date(date)
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.order_lines = order_lines if order_lines is not None else []

    def validate_date(self, date):
        if date < datetime.now():
            raise ValueError("Order date cannot be in the past.")
        return date

    def calculate_total_amount(self):
        return sum(line.subtotal for line in self.order_lines if line.subtotal is not None)

    def display_order_info(self):
        print(f"Order Information: {self.number}, {self.date}, {self.calculate_total_amount()}, {self.company.name if self.company else 'N/A'}, {self.billing.name if self.billing else 'N/A'}, {self.shipping.name if self.shipping else 'N/A'}")
        print("Order Lines:")
        for line in self.order_lines:
            print(line.display_order_line_info())

def display_all_orders(orders, title="All Orders"):
    print(f"\n=== {title} ===")
    for order in orders:
        order.display_order_info()
        print()

def sort_orders_by_date_desc(orders):
    sorted_orders = sorted(orders, key=lambda order: order.date, reverse=True)
    print("\nSorted Orders by Date (Descending):")
    return sorted_orders

def filter_current_month_orders(orders):
    current_month = datetime.now().month
    return [order for order in orders if order.date.month == current_month]

def search_orders_by_number(orders, number):
    return [order for order in orders if order.number == number]

def list_orders_of_specific_product(orders, product):
    return [order for order in orders for line in order.order_lines if line.product == product]

customer1 = Customer(name="JK", email="jk@gmail.com", phone="1234567890", city="Cityville", state="Stateville", country="Countryland")
customer2 = Customer(name="JP", email="jp@gmail.com", phone="9876543210", city="Business City", state="Corporate State", country="Companyland", type="company")

order_lines1 = [
    OrderLine(product="Product A", quantity=2, price=10.00),
    OrderLine(product="Product B", quantity=1, price=20.00),
    OrderLine(product="Product C", quantity=3, price=5.00)
]

order_lines2 = [
    OrderLine(product="Product D", quantity=1, price=15.00),
    OrderLine(product="Product B", quantity=2, price=20.00),
    OrderLine(product="Product E", quantity=4, price=7.50)
]

order1 = Order(number="12345", date=datetime.now() + timedelta(days=2), company=customer2, billing=customer1, shipping=customer1, order_lines=order_lines1)
order2 = Order(number="67890", date=datetime.now() + timedelta(days=5), company=customer2, billing=customer2, shipping=customer2, order_lines=order_lines2)

limited_orders = [order1, order2]

# Display Order and Customer Information
customer1.display_customer_info()
order1.display_order_info()

# Display all unique products
unique_products = set(line.product for order in limited_orders for line in order.order_lines)
print("\nUnique Products:")
for product in unique_products:
    print(product)

# Sort orders based on "date" in descending order
sorted_orders_desc = sort_orders_by_date_desc(limited_orders)
display_all_orders(sorted_orders_desc, title="Sorted Orders")

# Filter current month orders
current_month_orders = filter_current_month_orders(limited_orders)
display_all_orders(current_month_orders, title="Current Month Orders")

# Search Orders by number
searched_orders = search_orders_by_number(limited_orders, "67890")
display_all_orders(searched_orders, title="Searched Orders")

# List/Display all orders of a specific product
specific_product_orders = list_orders_of_specific_product(limited_orders, "Product B")
display_all_orders(specific_product_orders, title="Specific Product Orders")
