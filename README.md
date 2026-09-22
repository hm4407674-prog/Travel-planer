🌍 Travel Planner

An interactive travel-planning web application built with Python and Streamlit that helps users explore destinations, view destination coordinates, check current weather and a 5-day forecast, manage a travel budget, and visualize destinations on an interactive map.

🚀 Live Demo

🔗 "Open Travel Planner" (https://travel-planer-kamut4bms85v3obf7e5fsj.streamlit.app/)

# Application Preview

The application provides an interactive travel-planning interface where users can enter a destination and explore its location, weather conditions, forecast, and travel budget.

# Destination & Weather

The application displays:

-  Destination name and coordinates
-  Current temperature
- Current wind speed
-  Travel budget
-  5-day weather forecast
-  Interactive destination map

# Features

- 🔍 Destination Search — Search for a destination by name.
-  Geographic Coordinates — Display the latitude and longitude of the selected destination.
-  Current Weather — View the current temperature for the selected destination.
- Wind Information — Display current wind speed.
-  5-Day Forecast — View daily high and low temperatures for the next five days.
-  Travel Budget — Set and manage a total travel budget.
-  Interactive Map — Visualize the selected destination on an interactive map.
-  Interactive Web Interface — Built with Streamlit for an accessible browser-based experience.

# Tech Stack

Programming Language

- Python 3.x

Framework

- Streamlit

Libraries

- Requests — Communicating with external APIs
- Pandas — Data processing and presentation
- Folium — Interactive map visualization
- streamlit-folium — Integrating Folium maps with Streamlit

APIs

- Open-Meteo — Weather data and forecasts
- Open-Meteo Geocoding API — Destination search and geographic coordinates

# How It Works

The application follows this workflow:

Enter Destination
       ↓
Geocode Destination
       ↓
Retrieve Latitude & Longitude
       ↓
Request Weather Data
       ↓
Process Weather Information
       ↓
Display Destination Information
       ↓
Show Forecast & Interactive Map

Information Displayed

For a selected destination, Travel Planner provides:

Information| Description
 Destination| Selected travel destination
🌐 Coordinates| Latitude and longitude
Temperature| Current temperature
 Wind Speed| Current wind speed
 Travel Budget| User-defined total budget
 Forecast| 5-day high and low temperatures
Map| Interactive destination map

# Project Structure

Travel-planer-/
│
├── .devcontainer/
│
├── README.md
├── Travel_app.py
└── requirements.txt

#  Installation

1. Clone the repository

git clone https://github.com/hm4407674-prog/Travel-planer-.git

2. Navigate to the project directory

cd Travel-planer-

3. Install the required dependencies

pip install -r requirements.txt

4. Run the application

streamlit run Travel_app.py

The application will open in your browser through the local Streamlit server.
# API Configuration

Travel Planner uses the Open-Meteo API for weather and geocoding data.

No API key is required for the public Open-Meteo services used by this application.

Weather data is provided by:

Open-Meteo

# Example

A user can enter a destination such as:

Tokyo

The application can then display information including:

Tokyo, Japan

Coordinates:
35.6895, 139.6917

Current Temperature:
21.7 °C

Wind Speed:
4.6 km/h

Travel Budget:
$2,000

5-Day Weather Forecast:
Daily high and low temperatures

The destination can also be visualized on an interactive map.

# Project Purpose

Travel Planner was developed to demonstrate the practical use of:

- Python programming
- Web application development
- API integration
- Data processing
- Interactive data visualization
- Geographic mapping
- Real-time weather data retrieval

The project combines these technologies into a single practical travel-planning application.

#  Future Improvements

Possible future improvements include:

-  Flight information integration
-  Hotel and accommodation information
-  Restaurant recommendations
-  Currency conversion
-  More detailed destination information
-  More advanced travel-budget planning
-  Personalized travel recommendations
-  Further improvements to the mobile user experience

# What I Learned

Through this project, I practiced:

- Building interactive applications with Streamlit
- Working with REST APIs
- Retrieving and processing real-time weather data
- Working with geographic coordinates
- Creating interactive maps with Folium
- Integrating external data into a web application
- Organizing a Python project for deployment
- Deploying a Streamlit application

🌐 Project Links

-  Live Demo: https://travel-planer-kamut4bms85v3obf7e5fsj.streamlit.app/
- 💻 GitHub Repository: https://github.com/hm4407674-prog/Travel-planer
- LinkedIn: https://www.linkedin.com/in/hafiz-mohammed-b6ba36433
