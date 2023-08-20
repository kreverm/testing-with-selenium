from retrying import retry

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser:
    """
    Base class for Selenium testing.
    Supports Chrome only.
    """
    def __init__(self):
        self.chrome_browser = webdriver.Chrome()

    def navigate_to_url(self, url: str):
        self.chrome_browser.get(url)

    def current_url(self) -> str:
        return self.chrome_browser.current_url

    def wait_until_url_contains(self, text: str):
        """
        Wait until browser url contains some text
        :param text: text to contain
        :return:
        """
        WebDriverWait(self.chrome_browser, 5).until(EC.url_contains(text))

    def wait_for_element_presence(self, selector: str, by=By.CSS_SELECTOR):
        WebDriverWait(self.chrome_browser, 5).until(EC.presence_of_element_located((by, selector)))

    @retry(wait_fixed=2000, stop_max_attempt_number=5)
    def enter_text(self, selector: str, text: str, by=By.CSS_SELECTOR):
        self.wait_for_element_presence(selector=selector, by=by)
        self.chrome_browser.find_element(by, selector).send_keys(text)
        self.chrome_browser.find_element(by, selector).send_keys(Keys.UP)
