from .base_page import BasePage
from locators import Main


class TopMenu(BasePage):

    # Search 'About Us'
    def checkout_about_us_in_top_menu(self):
        assert self.presence_of_element(*Main.TopMenu.ABOUT_US) is True, "Кнопка 'О нас' отсутствует в DOM"
        assert self.visability_of_element(*Main.TopMenu.ABOUT_US) is True, "Кнопка 'О нас' отсутствует на стр."
        self.scroll(*Main.EnterMenu.IN_ABOUT_US)
        assert self.presence_of_element(*Main.EnterMenu.IN_ABOUT_US) is True, "Текс 'О нас' отсутствует в DOM"
        assert self.visability_of_element(*Main.EnterMenu.IN_ABOUT_US) is True, "Текст 'О нас' отсутствует на стр."

    # Search 'Project'
    def checkout_projects_in_top_menu(self):
        assert self.presence_of_element(*Main.TopMenu.PROJECTS) is True, "Кнопка 'Проекты' отсутствует в DOM"
        assert self.visability_of_element(*Main.TopMenu.PROJECTS) is True, "Кнопка 'Проекты' отсутствует на стр."
        self.scroll(*Main.EnterMenu.IN_PROJECTS)
        assert self.presence_of_element(*Main.EnterMenu.IN_PROJECTS) is True, "Текст 'Проекты' отсутствует в DOM"
        assert self.visability_of_element(*Main.EnterMenu.IN_PROJECTS) is True, "Текст 'Проекты' отсутствует на стр."

    # Search 'Mentors'
    def checkout_mentors_top_menu(self):
        assert self.presence_of_element(*Main.TopMenu.MENTORS) is True, "Кнопка 'Менторы' отсутствует в DOM"
        assert self.visability_of_element(*Main.TopMenu.MENTORS) is True, "Кнопка 'Менторы' отсутствует на стр."
        self.scroll(*Main.EnterMenu.IN_MENTORS)
        assert self.presence_of_element(*Main.EnterMenu.IN_MENTORS) is True, "Текст 'Менторы' отсутствует в DOM"
        assert self.visability_of_element(*Main.EnterMenu.IN_MENTORS) is True, "Текст 'Менторы' отсутствует на стр."

    # Search 'StartUp for'
    def checkout_startup_top_menu(self):
        assert self.presence_of_element(*Main.TopMenu.START_UP) is True, "Кнопка 'StartUp для' отсутствует в DOM"
        assert self.visability_of_element(*Main.TopMenu.START_UP) is True, "Кнопка 'StartUp для' отсутствует на стр."
        self.scroll(*Main.EnterMenu.IN_STARTUP)
        assert self.presence_of_element(*Main.EnterMenu.IN_STARTUP) is True, "Текст 'StartUp для' отсутствует в DOM"
        assert self.visability_of_element(*Main.EnterMenu.IN_STARTUP) is True, "Текст 'StartUp для' отсутствует на стр."