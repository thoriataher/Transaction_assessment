from datetime import datetime
from typing import List

class Item:
    def __init__(self, item_id,name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity
        
        def to_dict(self):
            return {
                'item_id': self.item_id,
                'name': self.name,
                'price': self.price,
                'quantity': self.quantity
            }
            
class Transaction:
    def __init__(self, transaction_id, date: datetime, customer_id, items: List[Item], total_amount):
        self.transaction_id = transaction_id
        self.date = date
        self.customer_id = customer_id
        self.items = items
        self.total_amount = total_amount
        
        def to_dict(self):
            return {
                'transaction_id': self.transaction_id,
                'date': self.date.strftime('%Y-%m-%d'),
                'customer_id': self.customer_id,
                'items': [item.to_dict() for item in self.items],
                'total_amount': self.total_amount
            }