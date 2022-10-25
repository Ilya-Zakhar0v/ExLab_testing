import time

from .base_page import BasePage
from .top_menu import TopMenu
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Main
from selenium import webdriver


class MainPage(BasePage):

    # Проверка URL
    def check_url(self):
        assert self.browser.current_url == self.url, 'Не корректный url'
        assert 'test.exlab.team' in self.browser.current_url, 'Не корректный url'

    # Dark Theme
    def background_color(self):
        black_background = 'sc-bczRLJ ckyTig'  # Аттрибут class (black theme)
        # white_background = 'sc-bczRLJ cxdoLY'
        assert self.browser.find_element(*Main.BLACK_BACKGROUND).get_attribute('class') == black_background, 'Некорретная тема лендинга (ОР: Black)'

    # Search Logo ExLab
    def lending_logo(self):
        assert self.element_is_visible(Main.LOGO), 'Логотип ExLab не найден'

    # Search Sun Icon
    def sun_icon(self):
        white_background = 'sc-bczRLJ cxdoLY'
        assert self.element_is_visible(Main.SUN_ICON), 'Sun Icon отсутствует'
        self.element_is_visible(Main.SUN_ICON).click()
        assert self.browser.find_element(*Main.WHITE_BACKGROUND).\
                   get_attribute('class') == white_background, 'Не корркетный цвет background (ОР: WHITE)'

    def language_button(self):
        pass

    def join_button(self):
        assert self.element_is_visible(Main.JOIN_BUTTON), 'Кнопка "Присоединиться" отсутствует'
        self.element_is_visible(Main.JOIN_BUTTON).click()
        first_window = self.browser.window_handles[1]
        self.browser.switch_to.window(first_window)
        assert self.browser.current_url == 'https://t.me/ExLab_registration_bot', 'Не тот урл'
        time.sleep(1)

        # assert self.browser.current_url == "https://t.me/ExLab_registration_bot", 'Не корректный url'
        # assert "t.me/ExLab_registration_bot" in self.browser.current_url, 'Не корректный url'

    def logo_for_otus(self):
        self.wait_for_visible(Main.LOGO)












# Отсутствие горизонтального скролла
#    def search_to_gorizont_scroll(self):
#       login_link = self.browser.

