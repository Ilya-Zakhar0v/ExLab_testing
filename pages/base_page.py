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

    def presence_of_element(self, by, value):
        """ Presence element in the DOM """
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((by, value)))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def visability_of_element(self, by, value):
        """ Element to be visibility """
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((by, value)))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def element_clickable(self, by, value):
        """ Element to be clickable """
        try:
            WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((by, value)))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def click_to_element(self, by, value):
        """ Click """
        try:
            self.browser.find_element(by, value).click()
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def scroll(self, by, value):
        """ Scroll to element (ActionChains) """
        try:
            elem = self.browser.find_element(by, value)
            time.sleep(0.5)
            ActionChains(self.browser).move_to_element(elem).perform()
            return True
        except NoSuchElementException:
            return False

    def scroll_to_element(self, by, value):
        """ Scroll to element (JS)"""
        try:
            element = self.browser.find_element(by, value)
            self.browser.execute_script("return arguments[0].scrollIntoView();", element)
            return True
        except NoSuchElementException:
            return False

    def check_window(self, browser):
        new_window = browser.window_handles
        if len(new_window) > 1:
            print(f'\nОткрыто {len(new_window)} вкладыки: {new_window}')
            browser.switch_to.window(new_window[1])  # Переместиться к нужной вкладке
            print(f'URL текущей вкладки: {browser.current_url}')
            obj = browser.switch_to.alert
            print(obj.text)
            #WebDriverWait(browser, 5).until(EC.alert_is_present())
            #alert = browser.switch_to.alert
            #print(alert.text)
            #if self.browser.switch_to.alert() in new_window:
                #print()



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
