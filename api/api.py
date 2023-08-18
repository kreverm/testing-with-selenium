import requests

WEATHER_API_KEY = "6e20848b7a7649e3992152753231808"  # Should not be inside code - ONLY FOR TESTING


def get_weather_data_by_zip_code_api(zip_code: str):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": WEATHER_API_KEY,
        "q": zip_code
    }

    return requests.get(base_url, params=params)
