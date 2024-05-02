import streamlit as st
import pydeck as pdk

# JavaScript to get user's geolocation
location_fetcher = """
<button onclick="getLocation()">Get Location</button>
<script>
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    console.log("Geolocation is not supported by this browser.");
  }
}
function showPosition(position) {
  document.getElementById('latitude').value = position.coords.latitude;
  document.getElementById('longitude').value = position.coords.longitude;
}
</script>
<input type="text" id="latitude" hidden>
<input type="text" id="longitude" hidden>
"""

# Streamlit component to fetch location
st.markdown(location_fetcher, unsafe_allow_html=True)

latitude = st.empty()
longitude = st.empty()

# Default location: Toronto, Canada
default_lat = 43.65107
default_lon = -79.347015

# Get user-provided location, if available
user_lat = st.text_input("Latitude", value="")
user_lon = st.text_input("Longitude", value="")

if user_lat and user_lon:
    latitude, longitude = float(user_lat), float(user_lon)
else:
    latitude, longitude = default_lat, default_lon

# Display the map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=latitude,
        longitude=longitude,
        zoom=11,
        pitch=50,
    ),
    layers=[],
))
