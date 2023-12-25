// src/App.js

import React, { useState } from 'react';
import axios from 'axios';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import './App.css'; // Assuming you have a CSS file for styling

const App = () => {
  const [buttonColor, setButtonColor] = useState('green');
  const [ledState, setLedState] = useState('on'); // Initial state is 'on'
  const [visiblePanels, setVisiblePanels] = useState([]);

    const handleMarkerClick = (index) => {
      setVisiblePanels((prevVisiblePanels) => {
        if (prevVisiblePanels.includes(index)) {
          // Si le panneau est déjà visible, le supprimer
          return prevVisiblePanels.filter((item) => item !== index);
        } else {
          // Sinon, ajouter le panneau
          return [...prevVisiblePanels, index];
        }
      });
    };

    const handleClick = async () => {
      try {
        // Toggle the LED state
        const newLedState = ledState === 'on' ? 'off' : 'on';
    
        // Make a POST request using Axios
        const response = await axios.get(`http://localhost:3000/led/${newLedState}`);
    
        // Check if the request was successful (status code 2xx)
        if (response.status === 200) {
          console.log(`LED turned ${newLedState}`); // Utiliser les backticks ici
          setLedState(newLedState); // Update the LED state
          setButtonColor(newLedState === 'on' ? 'red' : 'green'); // Update button color
        } else {
          console.error(`Failed to turn ${newLedState} LED:`, response.statusText);
        }
      } catch (error) {
        console.error('Error:', error.message);
      }
    };


  const MyMap = () => {
    const center = [33.2433, -8.4988]; // Coordinates for the initial center of the map
    const zoom = 13; // Initial zoom level
    const AlmorabitinCoords1 = [33.244646, -8.494815];
    const AlmorabitinCoords2 = [33.244219, -8.494961];
    
  

    const customIcon1 = new L.Icon({
      iconUrl: 'fr.png',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      shadowSize: [41, 41],
      
    });


    return  (
      <div className="map-container">
        {/* MapContainer est utilisé pour afficher la carte */}
        <MapContainer center={center} zoom={zoom} style={{ height: '1000px', width: '1000px' }}>
          {/* TileLayer est utilisé pour afficher les tuiles de la carte */}
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />
  
          {/* Marqueur pour le carrefour Almorabitin */}
          <Marker position={AlmorabitinCoords1} icon={customIcon1} interactive={true} eventHandlers={{ click: () => handleMarkerClick(0) }}>
          <Popup autoPan={false}>
            Almorabitin FeuRouge 1<br/>
          </Popup>
        </Marker>

        <Marker position={AlmorabitinCoords2} icon={customIcon1} interactive={true} eventHandlers={{ click: () => handleMarkerClick(1) }}>
          <Popup autoPan={false}>
            Almorabitin FeuRouge 2<br />
          </Popup>
        </Marker>

        </MapContainer>
              
       
      </div>
    );
  };
  
  const Panel = ({ onClick }) => {
    return (
      <div className="panel">
        <img
          src={ledState === 'on' ? 'led-on.gif' : 'led-off.png'}
          alt="LED"
          className="centered-image"
        />
        <button
          style={{ backgroundColor: buttonColor }}
          className="centered-button"
          onClick={handleClick}
        >
          Click me
        </button>
      </div>
    );
  };
  

  return (
    <div className="app-container" >
          <h1>Map de FeuRouge</h1>
          <MyMap/>
          {visiblePanels.map((index) => (
      <Panel key={index}  />
  ))}
    </div>
  );
};

export default App;
