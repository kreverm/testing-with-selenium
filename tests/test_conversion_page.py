import pytest
from web_pages.conversions_page import ConversionsPage


@pytest.mark.parametrize("conversion_type,conversion_form,value,expected_result", [
    (("Celsius", "Fahrenheit"), "Celsius to Fahrenheit", "10", "50.00000°F"),
    (("Celsius", "Fahrenheit"), "Celsius to Fahrenheit", "0", "32.00000°F"),
    (("Celsius", "Fahrenheit"), "Celsius to Fahrenheit", "", ''),
    (("Celsius", "Fahrenheit"), "Celsius to Fahrenheit", "abc", "32.00000°F"),
    (("Celsius", "Fahrenheit"), "Celsius to Fahrenheit", "#$%#$%", "32.00000°F"),
    (("Celsius", "Fahrenheit"), "Celsius to Fahrenheit", "-1000", "-1768.000°F"),
    (("Celsius", "Fahrenheit"), "Celsius to Fahrenheit", "1000", "1832.000°F"),
    (("Meters", "Feet"), "Meters to Feet", "10", "32ft 9.700788in"),
    (("Meters", "Feet"), "Meters to Feet", "0", "0ft 0.000000in"),
    (("Meters", "Feet"), "Meters to Feet", "", ''),
    (("Meters", "Feet"), "Meters to Feet", "abc", "0ft 0.000000in"),
    (("Meters", "Feet"), "Meters to Feet", "#$%#$%", "0ft 0.000000in"),
    (("Meters", "Feet"), "Meters to Feet", "-1000", "-3280ft -10.07880in"),
    (("Meters", "Feet"), "Meters to Feet", "1000", "3280ft 10.07880in"),
    (("Ounces", "Feet"), "Ounces to Grams", "10", "283.4952g"),
    (("Ounces", "Grams"), "Ounces to Grams", "0", "0.000000g"),
    (("Ounces", "Grams"), "Ounces to Grams", "", ''),
    (("Ounces", "Grams"), "Ounces to Grams", "abc", "0.000000g"),
    (("Ounces", "Grams"), "Ounces to Grams", "#$%#$%", "0.000000g"),
    (("Ounces", "Grams"), "Ounces to Grams", "-1000", "-28349.52g"),
    (("Ounces", "Grams"), "Ounces to Grams", "1000", "28349.52g"),

])
def test_conversion(conversion_type, conversion_form, value, expected_result):
    """
    Tests various conversions result.
    Seems like there is no limit on the text input of the converted values - so not testing it.

    :param conversion_type: Conversion type to use e.g (from, to)
    :param conversion_form: Conversion form to use for conversion
    :param value: test value
    :param expected_result: expected result
    :return:
    """
    page = ConversionsPage()
    data = page.DATA

    # Go to desired URL (conversions site)
    page.navigate_to_url(data.URL)
    # Enter desired conversion - from -> to
    page.enter_search_text(*conversion_type)
    # Find conversion form, enter value, redirect and extract the result text
    result = page.make_conversion(conversion_form, value)
    # Close the browser at the end of the test parameter run
    page.chrome_browser.quit()
    # Make an assertion
    assert result == expected_result
