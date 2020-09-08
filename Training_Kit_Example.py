# Training Kit Example
# Intro to Python III

from datetime import datetime

# This is our base user class 
# All our Users will inherhit from this class
class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin

class Admin(User):
    def __init__(self, name):
        # super method helps us inherit from the User class
        super().__init__(name, is_admin=True)

class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.purchases = []
    def purchase_product(self, product):
        purchase = Purchase(product, self)
        self.purchases.append(purchase)

class Vendor(User):
    def __init__(self, name):
        super().__init__(name)
        self.products = []
    def create_product(self, product_name, product_price):
        product = Product(product_name, product_price, self)
        self.products.append(product)

# Product & Purchase

class Product:
    def __init__(self, name, price, vendor):
        self.name = name
        self.price = price
        self.vendor = vendor

class Purchase:
    def __init__(self, product, customer):
        self.product = product
        self.customer = customer
        self.purchase_price = product.price
        self.purchase_data = datetime.now()

#
# Designing a parking lot
#

# Payments, capacity, vehicles, pricing.

class Vehicle:
    def __init__(self, make, model, year, tag):
        self.make = make
        self.model = model
        self.year = year
        self.tag = tag

class Payments:
    def __init__(self, cash, debit, credit, rewards):
        self.cash = cash
        self.debit = debit
        self.credit = credit
        self.rewards = rewards
    
class Capacity:
    def __init__(self, level, number):
        self.level = level
        self.number = number
    def full_lot(self, level, percent_full):
        #some function?
        level = 0

class Pricing:
    def __init__(self, hourly, daily, weekly):
        self.hourly = hourly
        self.daily = daily
        self.weekly = weekly



