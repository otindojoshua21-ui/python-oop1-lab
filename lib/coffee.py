#!/usr/bin/env python3

class Coffee:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
        self.total_tips = 0.0

    def tip(self, amount):
        self.total_tips += amount
        return f"Thank you for the ${amount:.2f} tip! Total tips: ${self.total_tips:.2f}."