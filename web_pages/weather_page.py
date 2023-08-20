""" Representation of www.weather.com main page """

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from web_pages.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WeatherPageData:
    URL = 'https://weather.com/'
    ZIP_CODE = '20852'
    TODAY_URL = '/today/'
    US_LOCATION = 'Rockville, MD'


class WeatherPage(Browser):
    PAGE_DATA = WeatherPageData
    SEARCH_FIELD_SELECTOR = 'LocationSearch_input'
    SEARCH_FIELD_LISTBOX_SELECTOR = 'LocationSearch_listbox'
    TEMPERATURE_SELECTOR = '.CurrentConditions--tempValue--MHmYY'

    @staticmethod
    def _search_list_of_elements_by_text_and_click(elements: list[WebElement], value_to_click: str):
        """ Utility function to find value in dropdown list """
        found = False
        for choice in elements:
            if value_to_click == choice.text:
                found = True
                choice.click()
                break

        if not found:
            raise f'No choice was found in dropdown by value: {value_to_click}'

    def search_and_return_temperature_value(self, text_to_search: str, value_to_select: str) -> float:
        """
        Searches for value in www.weather.com and returns today's temperature value
        Can select only by value in this implementation.

        List box search field should be implemented in a dedicated component class.
        This is only functional representation.

        :param text_to_search: text that you want to search
        :param value_to_select: select this value after searching
        :return: today's temperature value of desired search value (location)
        """
        wait = WebDriverWait(self.chrome_browser, 5)
        self.enter_text(self.SEARCH_FIELD_SELECTOR, text_to_search, By.ID)

        # Wait until dropdown will load
        dropdown = wait.until(EC.presence_of_element_located((By.ID, self.SEARCH_FIELD_LISTBOX_SELECTOR)))
        dropdown_options = dropdown.find_elements(By.CSS_SELECTOR, '[type="button"]')

        self._search_list_of_elements_by_text_and_click(dropdown_options, value_to_select)

        # Wait until redirected to Rockville page
        wait.until(EC.url_contains(self.PAGE_DATA.TODAY_URL))
        temperature_text = self.chrome_browser.find_element(By.CSS_SELECTOR, self.TEMPERATURE_SELECTOR).text

        return float(temperature_text.split('°')[0])
