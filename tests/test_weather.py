from api.api import get_weather_data_by_zip_code_api
from web_pages.weather_page import WeatherPage


def test_weather_difference():
    page = WeatherPage()
    data = WeatherPage.PAGE_DATA

    # API temperature
    api_temperature = get_weather_data_by_zip_code_api(zip_code=data.ZIP_CODE).json()['current']['temp_f']

    # UI temperature
    page.navigate_to_url(data.URL)
    ui_temperature = page.search_and_return_temperature_value(text_to_search=data.ZIP_CODE,
                                                              value_to_select=data.US_LOCATION)

    are_in_range_of_10_percent = ((api_temperature + (api_temperature * 0.1) >= ui_temperature) or
                                  (api_temperature - (api_temperature * 0.1) <= ui_temperature))

    assert are_in_range_of_10_percent is True
