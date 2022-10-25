import time

from selenium.webdriver.common.by import By
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.top_menu import TopMenu
from locators.Main import Main
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_landing_url(browser):
    """ № 1. Проверка url + Dark Theme """
    landing_url = MainPage(browser)
    landing_url.open()
    landing_url.check_url()
    landing_url.background_color()
    # Проверка всей ссылки
    # WebDriverWait(browser, 2).until(ec.url_to_be('http://test.exlab.team/'))


def test_landing_logo(browser):
    """ № 2. Отображение лого Ex-lab """
    logo = MainPage(browser)
    logo.open()
    logo.lending_logo()


def test_about_us(browser):
    """ № 3. Отображение ссылки <<О нас>> на гл. странце """
    about_us = MainPage(browser)
    about_us.open()
    top_menu = TopMenu(browser)
    top_menu.checkout_about_us_in_top_menu()


def test_projects(browser):
    """ № 4. Проверка отображение ссылки <<Проекты>> на гл. странце """
    projects = MainPage(browser)
    projects.open()
    top_menu = TopMenu(browser)
    top_menu.checkout_projects_in_top_menu()


def test_mentors(browser):
    """ № 5. Проверка отображение ссылки <<Менторы>> на гл. странце """
    mentors = MainPage(browser)
    mentors.open()
    top_menu = TopMenu(browser)
    top_menu.checkout_mentors_top_menu()


def test_start_up(browser):
    """ № 6. Проверка отображение ссылки <<StartUp for>> на гл. странце """
    start_up = MainPage(browser)
    start_up.open()
    top_menu = TopMenu(browser)
    top_menu.checkout_startup_top_menu()


def test_sun_icon(browser):
    """ № 7. Проверка отображение ссылки <<Sun Icon>> + click """
    sun_icon = MainPage(browser)
    sun_icon.open()
    sun_icon.sun_icon()


def test_language_button(browser):
    """ № 8. Проверка отображения кнопки переключения языка пользовательского интерфейса """
    pass


def test_join_button(browser):
    """ № 9. Отображение кнопки [Присоединиться] """
    page = MainPage(browser)
    page.open()
    page.join_button()





#def test_otus(browser):
    #page = MainPage(browser)
    #page.open()
    #page.logo_for_otus()



# Проверка отсутствия горизонтального скролла
# def test_not_scroll_in_landing(browser):
#    link = 'http://test.exlab.team/'
#    page = MainPage(browser=browser, url=link)
#    page.open()
#    page.


