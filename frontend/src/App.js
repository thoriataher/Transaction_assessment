import { useEffect, useState } from "react";
import "./App.css";
function App() {
  // use data to display the fetched transactions
  const [data, setData] = useState([]);

  const fetchData = async () => {
    const response = await fetch("http://127.0.0.1:5000/");
    const fetchedData = await response.json();
    setData(fetchedData);
  };
  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <h1>Welcome to UR-Store Assessment</h1>
      {/* implement the ui here */}
    </div>
  );
}

export default App;
