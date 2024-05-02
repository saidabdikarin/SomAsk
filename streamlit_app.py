import streamlit as st

# HTML and JavaScript to fetch geolocation
geolocation_script = """
<button onclick="getLocation()">Get Current Location</button>
<script type="text/javascript">
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(sendPosition);
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}
function sendPosition(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    // Use Streamlit's forms to submit these values back to the server
    document.querySelector("#latitude").value = latitude;
    document.querySelector("#longitude").value = longitude;
    document.querySelector("form").submit();
}
</script>
"""

# Use Streamlit's forms and inputs to capture the data
with st.form("location_form"):
    st.markdown(geolocation_script, unsafe_allow_html=True)
    # Hidden inputs to store the latitude and longitude
    lat = st.text_input("Latitude", "", key="latitude", type="hidden")
    lon = st.text_input("Longitude", "", key="longitude", type="hidden")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Latitude:", lat)
        st.write("Longitude:", lon)

if lat and lon:
    # Additional processing or mapping here if needed
    st.map(data=[[float(lat), float(lon)]], zoom=11)
else:
    st.write("No location provided, showing default location.")
    # Default to Toronto
    st.map(data=[[43.65107, -79.347015]], zoom=11)
