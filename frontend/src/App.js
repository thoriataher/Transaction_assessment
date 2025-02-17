import React, { useState } from "react";
import "./App.css";

function App() {
  const [groupBy, setGroupBy] = useState("customer_id");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [customerId, setCustomerId] = useState("");
  const [itemId, setItemId] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Construct query parameters
    const params = new URLSearchParams({ group_by: groupBy });
    if (startDate && endDate) {
      params.append("start_date", startDate);
      params.append("end_date", endDate);
    }
    if (customerId) {
      params.append("customer_id", customerId);
    }
    if (itemId) {
      params.append("item_id", itemId);
    }

    try {
      const response = await fetch(`http://127.0.0.1:5000/aggregate?${params.toString()}`);
      
      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }

      const data = await response.json();
      setResult(data);
      setError("");
    } catch (err) {
      setError(err.message || "An error occurred");
      setResult(null);
    }
  };

  return (
    <div className="App">
      <h1>Transaction Aggregator</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Group By:</label>
          <select value={groupBy} onChange={(e) => setGroupBy(e.target.value)}>
            <option value="customer_id">Customer ID</option>
            <option value="item_id">Item ID</option>
            <option value="date_range">Date Range</option>
            <option value="all">All Transactions</option>
          </select>
        </div>

        {groupBy === "date_range" && (
          <div>
            <label>Start Date:</label>
            <input
              type="date"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              required
            />
            <label>End Date:</label>
            <input
              type="date"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              required
            />
          </div>
        )}

        <div>
          <label>Customer ID:</label>
          <input
            type="number"
            value={customerId}
            onChange={(e) => setCustomerId(e.target.value)}
          />
        </div>

        <div>
          <label>Item ID:</label>
          <input
            type="number"
            value={itemId}
            onChange={(e) => setItemId(e.target.value)}
          />
        </div>

        <button type="submit">Submit</button>
      </form>

      {error && <p>{error}</p>}

      {result && (
        <div>
          <h2>Result:</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
