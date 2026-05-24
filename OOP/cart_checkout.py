from dataclasses import dataclass


@dataclass
class Product:
    price: float


#with None
@dataclass
class DiscountCoupon:
    rate: float


@dataclass
class Cart:
    products: list[Product]
    discount_coupon: DiscountCoupon
    
    def subtotal(self):
        return sum(product.price for product in self.products)
    
    def total(self):
        if self.discount_coupon is None:
            return self.subtotal()
        else:
            return self.subtotal() * (1 - self.discount_coupon.rate)


cart = Cart([Product(10.12), Product(3.78)], DiscountCoupon(0.15))
print(cart.total())
# 11.814999999999998

cart = Cart([Product(10.12), Product(3.78)], None)
print(cart.total())
# 13.899999999999999

# with NullObject
@dataclass
class DiscountCoupon:
    rate: float
    
    def discount(self, subtotal):
        return subtotal * (1 - self.rate)


@dataclass
class NullDiscountCoupon:
    def discount(self, subtotal):
        return subtotal


@dataclass
class Cart:
    products: list[Product]
    discount_coupon: DiscountCoupon
    
    def subtotal(self):
        return sum(product.price for product in self.products)
    
    def total(self):
        return self.discount_coupon.discount(self.subtotal())


cart = Cart([Product(10.12), Product(3.78)], DiscountCoupon(0.15))
print(cart.total())
# 11.814999999999998

cart = Cart([Product(10.12), Product(3.78)], NullDiscountCoupon())
print(cart.total())
# 13.899999999999999
