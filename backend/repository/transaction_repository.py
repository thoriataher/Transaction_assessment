import json
from datetime import datetime
from models.transaction import Transaction, Item
from typing import List, Dict

def get_filtered_transactions(filters: Dict = None) -> List[Transaction]:
    with open('data.json') as file:
        data = json.load(file)

    # If no filters provided, return all transactions
    if not filters:
        return [
            Transaction(
                transaction_id=txn["transaction_id"],
                customer_id=txn["customer_id"],
                date=txn["date"],
                items=[Item(**item) for item in txn["items"]],
                total_amount=txn["total_amount"]
            )
            for txn in data
        ]

    filtered_transactions = []

    for txn in data:
        match = True

        # Filter by customer_id if present
        if "customer_id" in filters:
            if str(txn["customer_id"]) != str(filters["customer_id"]):
                match = False

        # Filter by item_id if present
        if "item_id" in filters:
            target_item_id = int(filters["item_id"])
            item_found = any(item["item_id"] == target_item_id for item in txn["items"])
            if not item_found:
                match = False

        # Filter by date range if present
        if "date_range" in filters and isinstance(filters["date_range"], dict):
            txn_date = datetime.strptime(txn["date"], "%Y-%m-%d")
            start_date = datetime.strptime(filters["date_range"]["start"], "%Y-%m-%d")
            end_date = datetime.strptime(filters["date_range"]["end"], "%Y-%m-%d")
            if not (start_date <= txn_date <= end_date):
                match = False

        if match:
            # Filter items if item_id filter is present
            filtered_items = txn["items"]
            if "item_id" in filters:
                target_item_id = int(filters["item_id"])
                filtered_items = [item for item in txn["items"] if item["item_id"] == target_item_id]

            # Create Item objects only from filtered items
            items = [Item(**item) for item in filtered_items]

            # Create Transaction with filtered items
            transaction = Transaction(
                transaction_id=txn["transaction_id"],
                customer_id=txn["customer_id"],
                date=txn["date"],
                items=items,
                total_amount=txn["total_amount"]
            )
            filtered_transactions.append(transaction)

    return filtered_transactions
