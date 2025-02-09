# Vancouver Beaches E. coli Tracker

This web app provides real-time updates on E. coli levels at Vancouver beaches. It helps users determine which beaches are safe for swimming using a color-coded table and an interactive map.

## 🌐 Live Demo
**FrontEnd (React UI):** (https://19ndc2.github.io/Vancouver_Beaches_Ecoli_Tracker)  
**Backend (Flask API):** (https://vancouver-beaches-ecoli-tracker.onrender.com/beach_ecoli_data)

## Features
- 📊 **E. coli Data Table** - View color-coded water quality levels.
- 🗺️ **Interactive Map** - See beach locations and their status.
- 🔗 **Live Data Fetching** - Pulls the latest updates from Vancouver Coastal Health. Note updates are only provided by Vancouver Coastal Health from May to September
- 🌍 **Mobile-Friendly UI** - Works on desktop and mobile.

## Project Structure
```md
/VanEColiMonitor  
│── /backend             # Flask backend  
│   ├── beachLogic.py    # Main Flask app  
│   ├── beach_data_scraper.py  # Web scraper for E. coli reports  
│   ├── requirements.txt # Dependencies for the backend  
│   ├── Procfile         # Render deployment instructions  
│── /frontend            # React frontend  
│   ├── src/             # React source files  
│   │   ├── App.css      # Webpage CSS code  
│   │   ├── App.js       # Main react app  
│   │   ├── MapComponent.js   # Map functionality  
│   ├── public/          # Static assets   
│   ├── package.json     # React project dependencies   
│── README.md            # Project documentation
```

## 🛠 Tech Stack
- **Frontend:** React, Leaflet
- **Backend:** Flask, BeautifulSoup (Web Scaper)
- **Hosting:** GitHub Pages (Frontend), Render (Backend)

## ⚡️ Running Locally
### 1️⃣ Clone the Repository
git clone https://github.com/19ndc2/Vancouver_Beaches_Ecoli_Tracker.git  
cd Vancouver_Beaches_Ecoli_Tracker

### 2️⃣ Backend Setup (Flask)
cd backend  
pip install -r requirements.txt  
python beachLogic.py  
- Backend runs on http://127.0.0.1:5000/  

### 3️⃣ Frontend Setup (React)
cd frontend  
npm install  
npm start  
- Frontend runs on http://localhost:3000/  

