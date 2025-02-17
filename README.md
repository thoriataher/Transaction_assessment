# UR-Store Assessment

## Overview
This project is a web-based transaction analysis tool that allows users to fetch and filter transaction records based on various parameters such as customer ID, item ID, and date range. It consists of a **React frontend** and a **Flask backend** that work together to retrieve and display financial data.

## Features
- Fetch and display transaction data from an API.
- Filter transactions based on:
  - Customer ID
  - Item ID
  - Start Date
  - End Date
  - Grouping (for revenue over date range)
- Choose from different endpoints:
  - Revenue per customer
  - Total sales
  - Revenue over a date range

## Tech Stack
### Frontend:
- React.js (useState, useEffect for state management)
- Fetch API for making HTTP requests
- Basic CSS for styling

### Backend:
- Flask for API handling
- Python for data processing
- JSON for API responses

---

### Prerequisites
Ensure you have the following installed:
- **Node.js** and **npm** for frontend
- **Python** and **Flask** for backend


## 📂 Project Structure

### **Frontend (`frontend/`)**
- **`src/`**: Contains the React application source code.
  - **`App.js`**: Main React application file UI components.
  - **`index.js`**: Entry point for the React app.
  - **`App.css`**: Stylesheet for the React app.
  - **`package.json`**: Lists frontend dependencies and scripts.
### **Backend (`backend/`)**
- **`models/`**: Defines data models.
  - **`transaction.py`**: Defines `Transaction` and `Item` models.
- **`repository/`**: Handles data retrieval and filtering.
  - **`transaction_repository.py`**: Retrieves and filters transaction data.
- **`services/`**: Aggregates transaction data.
  - **`transaction_service.py`**: Contains logic for aggregating transactions.
- **`routes/`**: Defines API routes.
  - **`transaction_routes.py`**: Defines routes for transaction-related endpoints.
- **`data.json`**: Sample transaction data.
- **`app.py`**: Main Flask application file.
- **`requirements.txt`**: Lists Python dependencies for the Flask backend.
- **`README.md`**: Project documentation.


---

This markdown structure is clean and easy to read. You can copy and paste it into your `README.md` file or any other documentation. Let me know if you need further assistance! 🚀

