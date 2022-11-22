import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .top_menu import TopMenu
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from locators import Main


class MainPage(BasePage):
    locators = Main()
    # Проверка URL
    def check_landing_url(self):
        landing_url = self.browser.current_url
        assert landing_url == 'http://test.exlab.team/', f'Не корректный url, ожидаем: {landing_url}'
        assert 'test.exlab.team' in self.browser.current_url, f'Не корректный url, ожидаем: {landing_url}'

    # Dark Theme
    def background_color(self):
        black_background = 'sc-bczRLJ ckyTig'
        white_background = 'sc-bczRLJ cxdoLY'
        assert self.browser.find_element(*Main.DARK_BACKGROUND).get_attribute('class') == black_background,\
            'Некорретная тема лендинга (ОР: Black)'

    # Search Logo ExLab
    def lending_logo(self):
        assert self.presence_of_element(*Main.LOGO), 'Лого не найдено'

    # Search Sun Icon
    def sun_icon(self):
        white_background = 'sc-bczRLJ cxdoLY'
        assert self.presence_of_element(*Main.SUN_ICON) is True, "Икнонка 'Sun Icon' отсутствует в DOM"
        assert self.visability_of_element(*Main.SUN_ICON) is True, "Икнонка 'Sun Icon' не отображается на стр."
        # self.element_is_visible(Main.SUN_ICON).click()
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
        assert self.presence_of_element(*Main.LOGO_IN_BLOG) is True, 'Отсутствует лого ExLab в DOM'
        assert self.visability_of_element(*Main.LOGO_IN_BLOG) is True, 'Отсутствует отображение лого ExLab на стр.'

    def checkout_inscriptions_in_blog(self):
        # Надпись Твоя возможность
        test_elem = 'Твоя возможность'
        elem = self.get_element_text(*Main.INSCRIPTION_IN_BLOG)
        assert self.presence_of_element(*Main.INSCRIPTION_IN_BLOG) is True, f"Элемент {test_elem} отсутствует в DOM"
        assert self.visability_of_element(*Main.INSCRIPTION_IN_BLOG) is True, f"Элемент {test_elem} не отображается на стр."
        assert test_elem in elem, f'Элемент "{elem}" не найден'

        assert self.check_elem_in_text(*Main.INSCRIPTION_ALL) is True, "ОШИБКА"

        # assert self.search_text_elem_in(*Main.INSCRIPTION_ALL) is True, "Не найден"

        # assert "ПОЛУЧИТЬ ТОТ САМЫЙ ОПЫТ" in all_elem, 'no'
        # assert "ПОРАБОТАТЬ В КОМАНДЕ" in all_elem, 'no'
        # assert "СОЗДАТЬ ПРОЕКТ С НУЛЯ" in all_elem, 'no'
        # assert "ПОПОЛНИТЬ ПОРТФОЛИО" in all_elem, 'no'



        # Текст под надписью Твоя возможность
        #text_in_elem = self.get_element_text(*Main.INSCRIPTION_ALL)
        #assert 'ПОЛУЧИТЬ ТОТ САМЫЙ ОПЫТ' in text_in_elem, 'Текст не найден'
        #assert 'ПОРАБОТАТЬ В КОМАНДЕ' in text_in_elem, 'Текст не найден'
        #assert 'СОЗДАТЬ ПРОЕКТ С НУЛЯ' in text_in_elem, 'Текст не найден'
        #assert 'ПОПОЛНИТЬ ПОРТФОЛИО' in text_in_elem, 'Текст не найден'

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
        assert self.presence_of_element(*Main.Block.BTN_JOIN) is True, "Кнопка 'Присоединиться' отсутствует в DOM"
        self.scroll(*Main.Block.BTN_JOIN)
        assert self.element_clickable(*Main.Block.BTN_JOIN) is True, "Кнопка 'Присоединиться' не кликабельна"
        assert self.visability_of_element(*Main.Block.BTN_JOIN) is True, "Кнопка 'Присоединиться' не отображается"
        self.click_to_element(*Main.Block.BTN_JOIN)
        assert self.check_url_in_new_window() == "https://t.me/ExLab_registration_bot", \
            "Не корректный URL в новой вкладке"

    def check_text_in_projects(self):
        assert self.get_text_in_prop(self.locators.EnterMenu.IN_PROJECTS_TEXT, "textContent") == "Проекты", \
            "Текст Проекты отсутствует в DOM"
        self.scroll(*Main.EnterMenu.IN_PROJECTS_TEXT)
        assert self.visability_of_element(*Main.EnterMenu.IN_PROJECTS_TEXT) is True, "Текст 'Проекты' не отображается"

    def check_all_logo(self):
        assert self.presence_all_elements(self.locators.Block.ALL_LOGO_IN_BLOCK, prop="currentSrc")
        self.scroll(*Main.Block.LOGO_EASY_HELP)
        self.visability_all_elements(self.locators.Block.ALL_LOGO_IN_BLOCK)
















