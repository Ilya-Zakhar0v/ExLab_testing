import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait  # Явное ожидаение
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url="http://test.exlab.team/", timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # Не явное ожидаение, если элемент не найден ждем 5 сек

    def open(self):
        return self.browser.get(self.url)

    def get_element_text(self, by, value):
        return self.browser.find_element(by, value).text

    # Проверка элемента в DOM
    def presence_of_element(self, by, value, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, value)), message=f'Локатор {(by, value)} отсутствует в DOM')
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    # Проверка видимости элемента на странице
    def visability_of_element(self, by, value, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((by, value)), message=f'Локатор {(by, value)} не виден на странице')
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    # Scroll to be element
    def scroll_to_element(self, by, value):
        try:
            element = self.browser.find_element(by, value)
            self.browser.execute_script("return arguments[0].scrollIntoView();", element)
            return True
        except NoSuchElementException:
            return False

    # Clickable
    def click_to_elem(self, by, value):
        try:
            element = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((by, value)))
            # element = self.browser.find_element(by, value)
            # time.sleep(1)
            scroll = self.browser.execute_script("return arguments[0].scrollIntoView();", element)
            # WebDriverWait(self.browser, 7).until(EC.element_to_be_clickable(element))
            time.sleep(2)
            scroll.click()
            # return self.browser.execute_script("return arguments[0].scrollIntoView();", element)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def new_scroll_and_click(self, locator: tuple, timeout: int = 5):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(*locator)).click()


    """ ------------- OTUS ------------- """

    # def element(self, selector):
    # by = None
    # if link_text:
    #    by = By.LINK_TEXT
    # elif 'css' in selector.keys():
    #    by = By.CSS_SELECTOR
    #    selector = selector['css']
    # elif 'xpath' in selector.keys():
    #    by = By.XPATH
    #    selector = selector['xpath']
    # return self.browser.find_elements(selector)

    #    def click(self, selector):
    #        ActionChains(self.browser).move_to_element(self.element(selector)).click().perform()
    #
    #    def input(self, selector, value):
    #        element = self.element(selector)
    #        element.clear()
    #        element.send_keys(value)

    #    def wait_for_visible(self, selector, wait=3):
    #        return WebDriverWait(self.browser, wait).until(ec.visibility_of(self.element(selector)))

    """ ------------- OTUS ------------- """







#    def click(self, selector, index=0):
#        ActionChains(self.browser).move_to_element(self.element(selector, index)).click().perform()

#    def check_link_href(self, locator, href):
#        element = WebDriverWait(self, 10).until(ec.presence_of_element_located(locator))
#        element_href = element.get_property('href')
#        if element_href == href:
#            return True
#        else:
#            return False
