import time

from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .top_menu import TopMenu
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from locators import Main


class MainPage(BasePage):

    # Проверка URL
    def check_landing_url(self):
        landing_url = self.browser.current_url
        assert landing_url == 'http://test.exlab.team/', f'Не корректный url, ожидаем: {landing_url}'
        assert 'test.exlab.team' in self.browser.current_url, f'Не корректный url, ожидаем: {landing_url}'
        # assert WebDriverWait(self.browser, 5).until(ec.url_to_be('http://test.exlab.team/')), 'Не корректный url'

    # Dark Theme
    def background_color(self):
        black_background = 'sc-bczRLJ ckyTig'
        white_background = 'sc-bczRLJ cxdoLY'
        assert self.browser.find_element(*Main.DARK_BACKGROUND).get_attribute('class') == black_background,\
            'Некорретная тема лендинга (ОР: Black)'

    # Search Logo ExLab
    def lending_logo(self):
        assert self.is_element_present(*Main.LOGO), 'Лого не найдено'

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

    def checkout_logo_in_blog(self):
        assert self.element_is_visible(Main.LOGO_IN_BLOG), 'Отсутствует лого ExLab блоге'

    def checkout_inscriptions_in_blog(self):
        # Надпись Твоя возможность
        test_elem = 'Твоя возможность:'
        elem = self.get_element_text(*Main.INSCRIPTION_IN_BLOG)
        assert elem == test_elem, f'Элемент "{test_elem}" не найден'
        # Текст под надписью Твоя возможность
        text_in_elem = self.get_element_text(*Main.INSCRIPTION_ALL)
        assert 'ПОЛУЧИТЬ ТОТ САМЫЙ ОПЫТ' in text_in_elem, 'Текст не найден'
        assert 'ПОРАБОТАТЬ В КОМАНДЕ' in text_in_elem, 'Текст не найден'
        assert 'СОЗДАТЬ ПРОЕКТ С НУЛЯ' in text_in_elem, 'Текст не найден'
        assert 'ПОПОЛНИТЬ ПОРТФОЛИО' in text_in_elem, 'Текст не найден'

    def block_abouts_us(self):
        # Надпись О нас в блоке
        self.element_is_visible(Main.TopMenu.ABOUT_US).click()
        about_us = self.element(*Main.EnterMenu.IN_ABOUT_US)
        assert about_us.is_displayed(), 'Надпись "О нас" не отображается'
        assert about_us.text == 'О нас', 'Не верный текст надписи "О нас"'
        # Текст в блоке О нас
        text_about_us = self.browser.find_element(By.XPATH, "//p[@class='sc-cCsOjp cdaqyF']")
        assert text_about_us.is_displayed(), 'Текст в блоке "О нас" не отображается'
        assert "Мы стартовали в апреле 2022 года" in text_about_us.text, 'Текст отсутствует'

    def block_why_exlab(self):
        elem_why_exlab = self.element(*Main.Block.GO_TO_WHY)
        self.go_to_element(elem_why_exlab)

        # Отображение надписи Почему ExLab
        why_exlab = 'Почему ExLab?'
        assert why_exlab in elem_why_exlab.get_property('innerText'), "Не корректный вывод. ОР - 'Почему ExLab?'"

        # Отображение текста под надписью Почему ExLab?
        text_why_exlab_01 = 'Опыт стоит дорого, но не у нас. Участие в проектах бесплатное'
        text_why_exlab_02 = 'У нас есть те, кто умеет. Поддержка менторов от идеи до запуска проекта.'
        text_why_exlab_03 = 'Знаем, чего хотят рекрутеры.'
        text_why_exlab_04 = 'Создаём оригинальные проекты, придуманные нашими участниками.'

        assert text_why_exlab_01 in elem_why_exlab.get_property('innerText'), "Не корректный текст 01"
        assert text_why_exlab_02 in elem_why_exlab.get_property('innerText'), "Не корректный текст 02"
        assert text_why_exlab_03 in elem_why_exlab.get_property('innerText'), "Не корректный текст 03"
        assert text_why_exlab_04 in elem_why_exlab.get_property('innerText'), "Не корректный текст 04"

    def join_button_in_block(self):

        elem = self.is_element_present2(Main.Block.BTN_JOIN)
        self.go_to_element(elem)
        elem.click()
        time.sleep(4)











