# 📝 JSON Data Aggregation & Filtering  

## 🎯 Objective  
Your task is to process a list of JSON objects (transaction records) and perform aggregate operations based on a specific field (e.g., `customer_id`, `date_range`, `item_id`). Additionally, you will implement **filtering** so that users can specify which subset of the data they want to analyze.  

This task will test your ability to:  
- Parse and manipulate JSON data  
- Perform aggregations using **Python classes** (Bonus)  
- Implement **filtering** based on user input  
- Write efficient and readable Python code  

---

## 📌 Task Instructions  

### ✅ Implement the Following Aggregations  

1. **Total Revenue per Customer**  
   - Sum of `total_amount` for each `customer_id`.  

2. **Total Sales per Item**  
   - Sum of all `quantity` sold for each `item_id`.  

3. **Revenue Over a Date Range**  
   - Sum of `total_amount` for transactions within a specified **date range**.  

---

### 🎛 Implement Filtering Options  

The user should be able to **filter** the dataset based on:  
- **Customer ID** (`customer_id`)  
- **Item ID** (`item_id`)  
- **Date Range** (e.g., from `"2024-02-01"` to `"2024-02-10"`)  

---

### 💡 Expected Functionality  

1. **Allow users to choose a filter (or no filter at all).**  
2. **Perform aggregation on the filtered dataset.**  
3. **Return a JSON response with the aggregated results.**  

---

## 🔥 Bonus Challenge (Optional 🚀)  

1. **Use Object-Oriented Programming (OOP) in Python**  
   - Create a **class-based** approach to handle filtering and aggregation.  
   - Example:  
     ```python
     class TransactionAggregator:
         def __init__(self, transactions):
             self.transactions = transactions
         
         def filter_by_customer(self, customer_id):
             # Return filtered transactions for a given customer_id
             pass
         
         def aggregate_total_revenue(self):
             # Calculate revenue per customer
             pass
     ```  

2. **Sort results by highest revenue or sales.**  

---

## 📝 Sample JSON Data  

Use the following mock transactions as test data:  

```json
[
    {
        "transaction_id": "txn_1001",
        "customer_id": 2001,
        "date": "2024-02-10",
        "items": [
            {"item_id": 3001, "name": "Laptop", "price": 1000.0, "quantity": 1},
            {"item_id": 3002, "name": "Mouse", "price": 25.0, "quantity": 2}
        ],
        "total_amount": 1050.0
    },
    {
        "transaction_id": "txn_1002",
        "customer_id": 2002,
        "date": "2024-02-10",
        "items": [
            {"item_id": 3001, "name": "Laptop", "price": 1000.0, "quantity": 1}
        ],
        "total_amount": 1000.0
    },
    {
        "transaction_id": "txn_1003",
        "customer_id": 2001,
        "date": "2024-02-11",
        "items": [
            {"item_id": 3003, "name": "Keyboard", "price": 50.0, "quantity": 1}
        ],
        "total_amount": 50.0
    },
    {
        "transaction_id": "txn_1004",
        "customer_id": 2001,
        "date": "2024-02-10",
        "items": [
            {"item_id": 3001, "name": "Laptop", "price": 1000.0, "quantity": 1}
        ],
        "total_amount": 1000.0
    }
]
```  

---

## 🎯 Expected Output  

Example response when filtering for **customer_id = 2001**:  

```json
{
    "total_revenue_per_customer": {
        "2001": 2100.0
    },
    "total_sales_per_item": {
        "3001": 2,
        "3002": 2,
        "3003": 1
    },
    "date_range_revenue": {
        "start": "2024-02-10",
        "end": "2024-02-11",
        "total": 2100.0
    }
}
```  

---

## 📦 Deliverables  

- A **Python script** implementing the aggregations and filtering.  
- A **README** explaining your approach.  
- **Bonus:** If using **OOP**, document your class methods.  

---

## 🔥 Extra Tips  

✅ Use **dictionaries** for efficient lookups.  
✅ Use **date parsing** (`datetime.strptime`) to handle date filtering.  
✅ Write **clean, modular functions** for better code readability.  

---

**Good luck! 🚀**