from api.api import get_weather_data_by_zip_code_api


def test_weather_api():
    response = get_weather_data_by_zip_code_api(zip_code='20852')

    assert response.status_code == 200
