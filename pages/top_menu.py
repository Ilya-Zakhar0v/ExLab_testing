from .base_page import BasePage
from locators import Main
import time


class TopMenu(BasePage):

    # Search 'About Us'
    def checkout_about_us_in_top_menu(self):
        assert self.element_is_visible(Main.TopMenu.ABOUT_US), "Ссылка <<О нас>> отсутствует в топ меню"
        self.element_is_visible(Main.TopMenu.ABOUT_US).click()
        assert self.element_is_visible(Main.EnterMenu.IN_ABOUT_US), "Элемент <<О нас>> отсутствует в теле страницы"

    # Search 'Project'
    def checkout_projects_in_top_menu(self):
        assert self.element_is_visible(Main.TopMenu.PROJECTS), "Ссылка <<Проекты>> отсутствует в топ меню"
        self.element_is_visible(Main.TopMenu.PROJECTS).click()
        assert self.element_is_visible(Main.EnterMenu.IN_PROJECTS), "Элемент <<Проекты>> отсутствует в теле страницы"
        time.sleep(5)

    # Search 'Mentors'
    def checkout_mentors_top_menu(self):
        assert self.element_is_visible(Main.TopMenu.MENTORS), "Ссылка <<Менторы>> отсутствует в топ меню"
        self.element_is_visible(Main.TopMenu.MENTORS).click()
        assert self.element_is_visible(Main.EnterMenu.IN_MENTORS), "Элемент <<Менторы>> отсутствует в теле страницы"

    # Search 'StartUp for'
    def checkout_startup_top_menu(self):
        assert self.element_is_visible(Main.TopMenu.START_UP), "Ссылка <<StartUp для>> отсутствует в топ меню"
        self.element_is_visible(Main.TopMenu.MENTORS).click()
        assert self.element_is_visible(Main.EnterMenu.IN_STARTUP), "Элемент <<StartUp для>> отсутствует в теле страницы"
