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
        assert WebDriverWait(self.browser, 5).until(ec.url_to_be('http://test.exlab.team/')), 'Не корректный url'

    # Dark Theme
    def background_color(self):
        black_background = 'sc-bczRLJ ckyTig'
        # white_background = 'sc-bczRLJ cxdoLY'
        assert self.browser.find_element(*Main.DARK_BACKGROUND).get_attribute('class') == black_background,\
            'Некорретная тема лендинга (ОР: Black)'

    # Search Logo ExLab
    def lending_logo(self):
        assert self.element_is_visible(Main.LOGO), 'Лого не найдено'

    # Search Sun Icon
    def sun_icon(self):
        white_background = 'sc-bczRLJ cxdoLY'
        assert self.element_is_visible(Main.SUN_ICON), 'Sun Icon отсутствует'
        self.element_is_visible(Main.SUN_ICON).click()
        assert self.browser.find_element(*Main.WHITE_BACKGROUND).\
                   get_attribute('class') == white_background, 'Не корркетный цвет background (ОР: WHITE)'

    # Button Join
    def join_button(self):
        assert self.element_is_visible(Main.JOIN_BUTTON), 'Кнопка "Присоединиться" отсутствует'
        self.element_is_visible(Main.JOIN_BUTTON).click()
        first_window = self.browser.window_handles[1]
        self.browser.switch_to.window(first_window)
        assert self.browser.current_url == 'https://t.me/ExLab_registration_bot', 'Не корректный url'
        assert "t.me/ExLab_registration_bot" in self.browser.current_url, 'Не корректный url'

    def checkout_logo_in_blog(self):
        assert self.element_is_visible(Main.LOGO_IN_BLOG), 'Отсутствует лого ExLab блоге'

    def checkout_inscriptions_in_blog(self):
        assert self.element_is_visible(*Main.INSCRIPTION_IN_BLOG), 'Надпись "Твоя возможность" отсутствует'
        # assert self.element_is_visible(Main.ALL_INSCRIPTION_IN_BLOG), 'Надпись "Получить Тот самый опыт" не найдена'
        assert self.browser.find_element(*Main.ALL_INSCRIPTION_IN_BLOG).is_displayed(), 'нету'

    def block_abouts_us(self):
        assert self.element_is_visible(Main.TopMenu.ABOUT_US), "Ссылка <<О нас>> отсутствует в топ меню"
        self.element_is_visible(Main.TopMenu.ABOUT_US).click()
        assert self.browser.find_element(By.LINK_TEXT, 'стартовали').is_displayed()
        # assert self.element_is_visible(Main.EnterMenu.IN_ABOUT_US), "Надпись <<О нас>> отсутствует в блоке"
        # assert self.is_element_present_tes(Main.Block.TEXT_IN_BLOCK_ABOUT_US), 'В блоке нет текста'










# Отсутствие горизонтального скролла
#    def search_to_gorizont_scroll(self):
#       login_link = self.browser.

