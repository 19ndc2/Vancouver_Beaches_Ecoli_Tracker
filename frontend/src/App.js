import React, { useState, useEffect } from "react";
import './App.css';
import MapComponent from "./MapComponent";

function App() {
  const [beaches, setBeaches] = useState([]);

  //get beach data
  useEffect(() => {
    fetch("https://vancouver-beaches-ecoli-tracker.onrender.com/beach_ecoli_data")
    //fetch("http://127.0.0.1:5000/beach_ecoli_data")
      .then((res) => res.json())
      .then((data) => {
        console.log("API Response:", data);  // Debugging log
        setBeaches(data);  

      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);


  //update beach data on page when available
  useEffect(() => {
    console.log("Beaches State Updated:", beaches);
  }, [beaches]);

  return (
    <div className="container">
        <h1>Vancouver Beaches E. coli Tracker</h1>
        <div style={{ width: "100%", maxWidth: "1000px", margin: "auto" }}>
          <MapComponent beaches={beaches} />
        </div>

        <table>
        <thead>
          <tr>
              <th>Beach</th>              
              <th>Status</th>
              <th>E. coli Level MPN/100mL</th>
              <th>Sample date</th>
          </tr>
        </thead>
        <tbody>
          {beaches && beaches.map((beach, index) => (
              <tr key={index}>
                <td>{beach.name}</td>
                <td className={beach.status}>{beach.status}</td>                 
                <td>{beach.ecoli_level}</td>
                <td>{beach.sample_date}</td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
