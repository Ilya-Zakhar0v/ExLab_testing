import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait  # Явное ожидаение
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url="http://test.exlab.team/"):
        self.browser = browser
        self.url = url

    def open(self):
        return self.browser.get(self.url)

    def get_text_in_prop(self, locator, prop: str):
        """ Text in Property """
        try:
            elem = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(locator))
            print(f'\nRequests property: {elem.get_attribute(prop)}')
            return elem.get_attribute(prop)
        except TimeoutException:
            return False

            # Пустая строка
            # get_text = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((by, value)))
            # print(f"\nТекст аттрибута: {get_text.text}")
            # return get_text.text

            # Рабочий через аттрибут
            # get_text = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((by, value)))
            # print(f"\nТекст аттрибута: {get_text.get_attribute('textContent')}")
            # return get_text.get_attribute('textContent')

    def presence_of_element(self, by, value):
        """ Presence element in the DOM """
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((by, value)))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def presence_all_elements(self, locator, prop: str):
        """ Presence of all elements in the DOM """
        try:
            elements = WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located(locator))
            # for elem in elements:
            #     print(f"Property: {elem.get_property(prop)}")
            return True
        except TimeoutException:
            return False

    def visability_of_element(self, by, value):
        """ Element to be visibility """
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((by, value)))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def visability_all_elements(self, locator):
        """ All elements to be visibility """
        try:
            elements = WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located(locator))
            elem = elements.get_dom_attribute('src')
            print(elements)
            return True
        except TimeoutException:
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

    def check_url_in_new_window(self):
        """ Check URL in new window """
        all_windows = self.browser.window_handles
        if len(all_windows) != 1:
            new_window = self.browser.window_handles[1]
            print(f'\nOpen {len(all_windows)} windows: {all_windows}')
            self.browser.switch_to.window(new_window)
            try:
                url_in_new_windows = self.browser.current_url
                print(f"URL in new windows {url_in_new_windows}")
                return url_in_new_windows
            except TimeoutException:
                return False


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


"""WORKS"""
#    def check_elem_in_text(self, by, value, element: str, *args):
#        """ Поиск элемента среди текста стр. """
#        try:
#            locator = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((by, value)))
#            elem = str(locator.text)
#            my_split = elem.split(*args)
#            print("\nСписок найденых элементов:\n", my_split)
#            if element in my_split:
#                return True
#        except (NoSuchElementException, TimeoutException):
#            return False
