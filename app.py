import streamlit as st
import pandas as pd
import requests

# 1. Configuration
API_KEY = 'AIzaSyDn4sfKRbS2C1mPifVUnzhXSC7HhpeRETI'

lahore_locations = [
    {'location': 'Shahi Masjid', 'address': 'Fort Rd, Walled City of Lahore, Lahore, 54000, Pakistan'},
    {'location': 'Shahi Fort', 'address': 'H8Q8+745, Walled City of Lahore, Lahore, Pakistan'},
    {'location': 'Lahore Fort', 'address': 'H8Q7+56P, Fort Rd, Walled City of Lahore, Lahore, Pakistan'},
    {'location': 'Army Museum', 'address': 'Amjad Chauhdry Rd, Saddar Town, Lahore, Pakistan'},
    {'location': 'Jinnah Hospital', 'address': 'Ahmed, Usmani Rd, Faisal Town, Lahore, 54550, Pakistan'},
    {'location': 'Services Hospital', 'address': 'Services hospital, Shadman 1 Shadman, Lahore, 40050, Pakistan'},
    {'location': 'Fatima Memorial Hostpital', 'address': 'Shadman Rd, Ichhra Lahore, 54000, Pakistan'},
    {'location': 'Emporium Mall', 'address': '16M Abdul Haque Rd, Trade Centre Commercial Area Phase 2 Johar Town, Lahore, 54000, Pakistan'},
    {'location': 'Dolmen Mall', 'address': 'Plot#158, Sector A DHA Phase 6, Lahore, 54000, Pakistan'},
    {'location': 'Packages Mall', 'address': 'Main Walton Rd, Shahrah-E-Roomi Nishtar Town, Lahore, 54750, Pakistan'},
    {'location': 'Fast Nuces', 'address': '852-B Milaad St, Block B Faisal Town, Lahore, 54770, Pakistan'},
    {'location': 'King Edwerd', 'address': 'H897+X5V Chowk, Nila Gumbad Rd, Neela Gumbad Lahore, 54000, Pakistan'},
    {'location': 'UET', 'address': 'G.T Road, Staff Houses Engineering University Lahore, Lahore, 39161, Pakistan'}
]

# 2. Define Function at the TOP LEVEL so it's always available
def get_distance_mile(origin, destination):
    # Fixed syntax: used f-string properly and corrected "routers" typo to "routes"
    url = f"https://routes.googleapis.com/directions/v2:computeRoutes?key={API_KEY}"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-FieldMask": "routes.distanceMeters"
    }

    body = {
        "origin": {"address": origin},
        "destination": {"address": destination},
        "travelMode": "DRIVE"
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()

        # Google Routes API returns a list called 'routes' (not 'routers')
        meters = data["routes"][0]["distanceMeters"]
        miles = round(meters / 1609.34, 2)
        return miles
    except Exception as e:
        st.error(f"Error for {destination}: {e}")
        return None

# 3. UI Elements
st.title("Distance Finder (Routes API)")
st.write("Enter Your Starting Address")

with st.form("address_form"):
    street = st.text_input("Street")
    city = st.text_input("City")
    state = st.text_input("State")
    zip_code = st.text_input("Zip Code")
    submitted = st.form_submit_button("Submit")

# 4. Logical Execution: Everything depends on 'submitted'
if submitted:
    if not street or not city:
        st.error("Please enter at least a street and city.")
    else:
        user_address = f"{street}, {city}, {state}, {zip_code}"
        st.success(f"Calculating Distances from: {user_address}")

        results = []
        for loc in lahore_locations:
            miles = get_distance_mile(user_address, loc['address'])
            results.append({
                "Location": loc['location'],
                "Address": loc['address'],
                "Distance (mi)": miles
            })

        # Create DataFrame and display
        df = pd.DataFrame(results)
        # Sort by distance (dropping None values if API failed for some)
        df_sorted = df.dropna(subset=['Distance (mi)']).sort_values('Distance (mi)')
        st.dataframe(df_sorted)