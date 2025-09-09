import React, { useState, useEffect } from "react";
import './App.css';
import MapComponent from "./MapComponent";
import LoadingSpinner from "./LoadingSpinner";

function App() {
  const [beaches, setBeaches] = useState([]);
  const [loading, setLoading] = useState(true);
  
  //get beach data
  useEffect(() => {
    setLoading(true); //start loading
    fetch("https://vancouver-beaches-ecoli-tracker.onrender.com/beach_ecoli_data")
    //fetch("http://127.0.0.1:5000/beach_ecoli_data")
      .then((res) => res.json())
      .then((data) => {
        console.log("API Response:", data);  // Debugging log
        setBeaches(data);  

      })
      .catch((error) => console.error("Error fetching data:", error))
      .finally(() => {
        setLoading(false); //stop loading
      }
      );
  }, []);


  //update beach data on page when available
  useEffect(() => {
    console.log("Beaches State Updated:", beaches);
  }, [beaches]);
  
 

  return (
    <div className="container">
        <h1>Vancouver Beaches E. coli Tracker</h1>

        {/*Show loading spinner while waiting for backend response */}
        {loading ? (
          <div>
            <LoadingSpinner />
            <p>
              This demo runs on a free server, which sleeps when idle.
              </p>
              <p>
              The first load may take up to 1–2 minutes while the backend wakes up.              
              </p>
          </div>
        ) : (
          
          <>
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
        </>)}
    </div>
  );
}

export default App;
