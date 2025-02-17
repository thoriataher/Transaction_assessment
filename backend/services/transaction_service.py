from typing import List, Dict, Any, Tuple
from repository.transaction_repository import get_filtered_transactions
from models.transaction import Transaction

class TransactionAggregator:
    
    VALID_GROUP_BY = ["customer_id", "item_id", "date_range", "all"]
    
    @staticmethod
    def aggregate_transactions(group_by: str, filters: Dict = None) -> Tuple[Any, int]:
        if group_by not in TransactionAggregator.VALID_GROUP_BY:
            return {"error": "Invalid group_by parameter"}, 400
            
        filtered_transactions = get_filtered_transactions(filters)
        
        if group_by == "customer_id":
            return TransactionAggregator._aggregate_by_customer(filtered_transactions), 200
        elif group_by == "item_id":
            return TransactionAggregator._aggregate_by_item(filtered_transactions), 200
        elif group_by == "date_range":
            return TransactionAggregator._aggregate_by_date_range(filtered_transactions), 200
        elif group_by == "all":
            return TransactionAggregator._get_all_transactions(filtered_transactions), 200
    
    @staticmethod
    def _aggregate_by_customer(transactions: List[Transaction]) -> List[Dict[str, Any]]:
        revenue_by_customer = {}
        for txn in transactions:
            if txn.customer_id not in revenue_by_customer:
                revenue_by_customer[txn.customer_id] = 0
            revenue_by_customer[txn.customer_id] += txn.total_amount
            
        return [
            {"customer_id": key, "total_revenue": value}
            for key, value in sorted(
                revenue_by_customer.items(),
                key=lambda x: x[1],
                reverse=True
            )
        ]
    
    @staticmethod
    def _aggregate_by_item(transactions: List[Transaction]) -> List[Dict[str, Any]]:
        sales_by_item = {}
        
        for txn in transactions:
            if not txn.items:
                continue  # Skip transactions with no items
        
        for item in txn.items:                    
            return [
                {"item_id": key, "total_sales": value}
                for key, value in sorted(
                    sales_by_item.items(),
                    key=lambda x: x[1],
                    reverse=True
                )
            ]
    
    @staticmethod
    def _aggregate_by_date_range(transactions: List[Transaction]) -> Dict[str, float]:
        total_revenue = sum(txn.total_amount for txn in transactions)
        return {"total_revenue": total_revenue}
    
    @staticmethod
    def _get_all_transactions(transactions: List[Transaction]) -> List[Dict[str, Any]]:
        return [
            {
                "transaction_id": txn.transaction_id,
                "customer_id": txn.customer_id,
                "items": [
                    {
                        "item_id": item.item_id,
                        "quantity": item.quantity,
                        "price": item.price
                    }
                    for item in txn.items
                ],
                "total_amount": txn.total_amount,
                "date": txn.date
            }
            for txn in transactions
        ] if transactions else []