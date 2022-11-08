import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait  # Явное ожидаение
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, browser, url="http://test.exlab.team/", timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # Не явное ожидаение, если элемент не найден ждем 5 сек

    def open(self):
        return self.browser.get(self.url)

    def get_element_text(self, how, what):
        return self.browser.find_element(how, what).text

    def presence_of_element(self, locator, timeout=5):
        try:
            elem = WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(locator),
                                                              message=f'Локатор {locator} не найден')
        except NoSuchElementException:
            return False
        return True

    # Перемещение скролла к элеменету
    def go_to_element(self, element):
        return self.browser.execute_script("return arguments[0].scrollIntoView();", element)

    # Поиск элемента
    def element(self, how, what):
        return self.browser.find_element(how, what)

    def wait_for_visible(self, how, what, timeout=5):
        return WebDriverWait(self.browser, timeout).until(ec.visibility_of(self.element(how, what)))

    def click(self, how, what):
        ActionChains(self.browser).move_to_element(self.element(how, what)).click().perform()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException('Элемент не найден'):
            return False
        return True

    def is_element_present2(self, element):
        try:
            self.browser.find_element(*element)
        except NoSuchElementException('Элемент не найден'):
            return 'False'
        return self.browser.find_element(*element)

    # Перейти к элементу
    def move_to_element(self, element, timeout=5):
        try:
            btn = wait(self.browser, timeout).until(ec.element_to_be_clickable(element))
            btn.click()
        except NoSuchElementException:
            return False
        return True

    # Ждем пока все элементы не будут видимы
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.browser, timeout).until(ec.visibility_of_all_elements_located(locator))

    # Поиск скрытого элемента
    def element_is_present(self, locator, timeout=10):
        return wait(self.browser, timeout).until(ec.presence_of_element_located(locator))

    # Поиск всех элементов
    def element_are_present(self, locator, timeout=10):
        return wait(self.browser, timeout).until(ec.presence_of_all_elements_located(locator))

    # Кликабельный элемент
    def element_is_clickable(self, locator, timeout=10):
        return wait(self.browser, timeout).until(ec.element_to_be_clickable(locator))

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

    # Клик по элементу
#    def click(self, selector):
#        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable())
#        ActionChains(self.browser).move_to_element(self.browser(selector)).click().perform()



#    def click(self, selector, index=0):
#        ActionChains(self.browser).move_to_element(self.element(selector, index)).click().perform()


# Проверка видимости элемента на странице
# How - как, what - какие
#    def element_is_visible(self, how, what):
#        try:
#            WebDriverWait(self, 20).until(ec.visibility_of_element_located((how, what)))
#        except TimeoutException:
#            return False
#        return True

#    def check_link_href(self, locator, href):
#        element = WebDriverWait(self, 10).until(ec.presence_of_element_located(locator))
#        element_href = element.get_property('href')
#        if element_href == href:
#            return True
#        else:
#            return False
