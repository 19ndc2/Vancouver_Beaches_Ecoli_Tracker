import React from "react";
import { MapContainer, TileLayer, CircleMarker, Popup } from "react-leaflet";

function MapComponent({beaches}) {
    const vancouverPosition = [49.2827, -123.1207]; //start position
    return(
        <MapContainer center={vancouverPosition} zoom={12} style={{ height: "500px", width: "100%" } } className="leaflet-container ">
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />

            {beaches.map((beach, index) => (
                <CircleMarker
                    key={index}
                    center={[beach.latitude, beach.longitude]}
                    //icon={getMarkerIcon(beach.status)} // Assign the custom icon
                    radius = {8}
                    fillOpacity={0.8}
                    color={
                        beach.status.toLowerCase() === "safe" ? "green" :
                        beach.status.toLowerCase() === "caution" ? "yellow" :
                        beach.status.toLowerCase() === "unsafe" ? "red" :
                        "gray" // Default for pending
                      }
                >
                <Popup>
                    <strong>{beach.name}</strong> <br />
                    E. coli Level: {beach.ecoli_level} <br />
                    Status: {beach.status} <br />
                    Sample Date: {beach.sample_date}
                </Popup>
                </CircleMarker>
                ))}




        </MapContainer>

        
    );
}
export default MapComponent;
