import requests
api_key = "c5162771e4fd7221cfb8b2405808a757"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"


def fetch_data():
    print("Sending API request...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response recieved successfully")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
#fetch_data()

def mock_fetch_data():
    return{'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-01-13 07:33', 'localtime_epoch': 1768289580, 'utc_offset': '-5.0'}, 'current': {'observation_time': '12:33 PM', 'temperature': -1, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '07:19 AM', 'sunset': '04:51 PM', 'moonrise': '03:06 AM', 'moonset': '12:24 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 28}, 'air_quality': {'co': '349.85', 'no2': '30.85', 'o3': '30', 'so2': '24.45', 'pm2_5': '19.35', 'pm10': '19.55', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 13, 'wind_degree': 255, 'wind_dir': 'WSW', 'pressure': 1020, 'precip': 0, 'humidity': 61, 'cloudcover': 25, 'feelslike': -5, 'uv_index': 0, 'visibility': 16, 'is_day': 'yes'}}
