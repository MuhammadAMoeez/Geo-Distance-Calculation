📍 Geo Distance Finder & Route Optimizer
A high-precision geospatial tool designed to calculate real-time travel distances, durations, and optimized routes between multiple global locations.

🎯 Project Motivation
Manual route planning for logistics or travel is prone to error and inefficiency. I built this tool to automate the complex process of calculating distance matrices, helping users identify the most efficient travel paths based on live traffic and various transport modes.

🚀 Key Features
Multi-Point Distance Matrix: Calculate distances and travel times for multiple origin-destination pairs simultaneously.

Spherical Geometry Calculations: Implements geodesic formulas to account for the Earth's curvature, ensuring accuracy over long distances.

Live Traffic Integration: Fetches real-time duration estimates based on current traffic conditions for driving modes.

Diverse Transport Support: Supports routing for driving, walking, bicycling, and public transit.

Interactive Streamlit UI: A clean interface for inputting addresses or coordinates and visualizing results instantly.

🛠️ Tech Stack
Language: Python 3.x.

Framework: Streamlit (Web Interface).

APIs: Google Maps Distance Matrix API (RESTful integration).

Libraries: geopy (Geocoding), pandas (Data handling), requests.

⚙️ How It Works
Input: User enters multiple origins and destinations as text addresses or Latitude/Longitude coordinates.

Geocoding: The app uses geopy to convert addresses into precise coordinates.

API Call: A request is sent to the Google Maps Distance Matrix API with parameters for travel mode and units.

Processing: The script parses the returned JSON payload to extract distance (meters/km) and duration (seconds/minutes).

Output: Results are displayed in a clean table and an interactive map.

📦 Installation
Clone the repository.

Install dependencies:

Bash

pip install streamlit pandas geopy requests
Add your Google Maps API Key to your environment variables or secrets.toml.

Launch the app:

Bash

streamlit run app.py
