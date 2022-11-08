from .base_page import BasePage
from locators import Main
import time
from selenium.webdriver.common.by import By


class TopMenu(BasePage):

    # Search 'About Us'
    def checkout_about_us_in_top_menu(self):
        assert self.is_element_present(*Main.TopMenu.ABOUT_US) is True, "Ссылка <<О нас>> отсутствует в топ меню"
        self.click(*Main.TopMenu.ABOUT_US)
        assert self.is_element_present(*Main.EnterMenu.IN_ABOUT_US) is True, "Элемент <<О нас>> отсутствует на странице"

    # Search 'Project'
    def checkout_projects_in_top_menu(self):
        assert self.is_element_present(*Main.TopMenu.PROJECTS) is True, "Ссылка <<Проекты>> отсутствует в топ меню"
        self.click(*Main.TopMenu.PROJECTS)
        assert self.is_element_present(*Main.EnterMenu.IN_PROJECTS) is True, "Элемент <<Проекты>> отсутствует на странице"
        time.sleep(2)


    # Search 'Mentors'
    def checkout_mentors_top_menu(self):
        assert self.element_is_visible(Main.TopMenu.MENTORS), "Ссылка <<Менторы>> отсутствует в топ меню"
        assert self.element_is_clickable(Main.TopMenu.MENTORS), "Ссылка не кликабельна"
        self.element_is_visible(Main.TopMenu.MENTORS).click()
        assert self.element_is_visible(Main.EnterMenu.IN_MENTORS), "Элемент <<Менторы>> отсутствует в теле страницы"

    # Search 'StartUp for'
    def checkout_startup_top_menu(self):
        assert self.element_is_visible(Main.TopMenu.START_UP), "Ссылка <<StartUp для>> отсутствует в топ меню"
        assert self.element_is_clickable(Main.TopMenu.START_UP), "Ссылка не кликабельна"
        self.element_is_visible(Main.TopMenu.MENTORS).click()
        assert self.element_is_visible(Main.EnterMenu.IN_STARTUP), "Элемент <<StartUp для>> отсутствует в теле страницы"
        # self.go_to_element()
        time.sleep(2)


