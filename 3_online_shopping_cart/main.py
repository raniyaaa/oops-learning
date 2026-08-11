from datetime import date
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CartItem:
    def __init__(self,product, quantity):
        self.product = product
        self.quantity = quantity
      #product does not magically mean the Product class. It becomes a reference to a Product object because you will pass p1 (which is a Product object) into that parameter.
    def get_price(self):
        return self.product.price * self.quantity

class Coupon:
    def __init__(self, code, discount, min_purchase, expiry):
        self.code = code
        self.discount = discount 
        self.min_purchase = min_purchase
        self.expiry = expiry
    def apply(self, total):
        if total < self.min_purchase:
            return total
        if date.today() > self.expiry:
            return total
        
        return max(0, total - self.discount)
        
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.coupons = []
    def add_item(self, product, quantity):
        item = CartItem(product, quantity)
        self.items.append(item)
    def remove_item(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                self.items.remove(item)
                break
    def total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total
    def add_coupon(self, coupon):
        self.coupons.append(coupon)
    def final_price(self):
        total = self.total()
        for coupon in self.coupons:
            total = coupon.apply(total)
        return total

class User:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)

user = User("Raniya")

user.cart.add_item(p1, 1)
user.cart.add_item(p2, 2)

print(user.cart.total())
coupon = Coupon(
    "SAVE1000",
    1000,
    50000,
    date(2026, 12, 31)
)

user.cart.add_coupon(coupon)
print(user.cart.final_price())
