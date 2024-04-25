import requests 
import streamlit as st 
import pandas as pd 

# Customer CSS
st.markdown(
    """
    <style>
    .fullScreenFrame > div[data-baseweb="modal"] > div > div > div {
        max-width: 100% !important;
        width: 100% !important;
    }
    :root {
    --primary-color: #f63366;
    --background-color: #5472ad;
    --secondary-background-color: #1a1b25;
    --text-color: #262730;
    --font: sans-serif;

}
    </style>
    """,
    unsafe_allow_html=True
)

# Fetch weather data from API
API_KEY = "d92180f646e34281a1c01240241004"

def fetch_weather():
    locations = ['Bangkok', 'Sydney', 'London', 'Tokyo']
    weather_data = []
    for location in locations:
        response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}')
        data = response.json()
        weather_data.append({
            'location': location,
            'temperature': data['current']['temp_c'],
            'weather_icon': data['current']['condition']['icon']
        })
    return weather_data 

# Stremlit UI
def main():
    st.title("Weather Report Live")
    st.write("Current Weather Conditions")
    
    # Fetch weather data
    weather_data = fetch_weather()
    df_weather = pd.DataFrame(weather_data)
    
    # Display weather data
    weather_rows = []
    for index, row in df_weather.iterrows():
        image = row['weather_icon']
        weather_rows.append(
            f"![Weather Icon]({image}) **City:** {row['location']} **Temperature:** {row['temperature']} C\n"
        )
        
    st.write("\n".join(weather_rows), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
