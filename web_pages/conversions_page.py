import time
from typing import Optional, Any, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from web_pages.browser import Browser


class ConversionsPageData:
    URL = "https://www.metric-conversions.org/"
    CONVERSION_URL_VALUE = ".htm"
    CELSIUS_TO_F_HEADER = "Celsius to Fahrenheit"
    CELSIUS = "Celsius"
    FAHRENHEIT = "Fahrenheit"
    METERS_TO_FEET_HEADER = "Meters to Feet"
    METERS = "Meters"
    FEET = "Feet"
    OUNCES_TO_GRAMS_HEADER = "Ounces to Grams"
    OUNCES = "Ounces"
    GRAMS = "Grams"


class ConversionsPage(Browser):
    DATA = ConversionsPageData
    ID_SEARCH_FROM = "queryFrom"
    ID_SEARCH_TO = "queryTo"
    ID_ANSWER = "answer"

    def __init__(self):
        super().__init__()

    def enter_search_text(self, from_text: str, to_text: str):
        # Enter text for both FROM field and TO field, e.g - FROM=Celsius, TO=Fahrenheit
        self.enter_text(self.ID_SEARCH_FROM, from_text, By.ID)
        self.enter_text(self.ID_SEARCH_TO, to_text, By.ID)

    def _find_conversion_form_by_title(self, title: str) -> Optional[WebElement]:
        # Find conversion form by title, e.g "Celsius to Fahrenheit" form
        time.sleep(3)  # Wait until DOM has changed - can be designed with "wait until"
        elements = self.chrome_browser.find_element(By.ID, "results").find_elements(By.CSS_SELECTOR, 'li')
        for element in elements:
            if element.find_element(By.CSS_SELECTOR, 'h2').text == title:
                return element

        return None

    def make_conversion(self, form_title: str, text: str) -> Union[bool, Any]:
        # Find a conversion form and return conversion result
        element = self._find_conversion_form_by_title(form_title)
        self.wait_for_element_presence('.convert', by=By.CSS_SELECTOR)
        element.find_element(By.CSS_SELECTOR, '.argument').send_keys(text)
        element.find_element(By.CSS_SELECTOR, '.convert').click()
        # Click on conversion and wait for redirect
        self.wait_until_url_contains(self.DATA.CONVERSION_URL_VALUE)

        return self.chrome_browser.find_element(By.ID, self.ID_ANSWER).text.split("= ")[-1]
