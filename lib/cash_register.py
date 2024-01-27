#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.total += price

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_price = self.total - self.price_of_last_transaction()
            self.total -= last_price
            self.items.pop()

    def price_of_last_transaction(self):
        if self.items:
            return self.total - sum(item_cost for item_cost in self.items_cost()[:-1])
        else:
            return 0

    def items_cost(self):
        return [1 for _ in self.items]
