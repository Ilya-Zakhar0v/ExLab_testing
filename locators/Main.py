from selenium.webdriver.common.by import By


class Main:

    DARK_BACKGROUND = (By.XPATH, "//div[@class='sc-bczRLJ ckyTig']")
    WHITE_BACKGROUND = (By.XPATH, "//div[@class='sc-bczRLJ cxdoLY']")
    LOGO = (By.XPATH, "//div[@class='sc-gKXOVf kORzJB']/div[@id='logo_mobile']")

    LOGO_2 = {"xpath": "//div[@class='sc-gKXOVf kORzJB']/div[@id='logo_mobile']"}

    SUN_ICON = (By.XPATH, "//div[@class='sc-fnykZs fEkGUM']")
    LANGUAGE_BUTTON = (By.XPATH, "jhghg")
    JOIN_BUTTON_NOT_CLICK = (By.XPATH, "//div[@class='sc-gKXOVf kORzJB']/div[@id='logo_mobile']")
    JOIN_BUTTON = (By.XPATH, "//div[@class='sc-hAZoDl hrEelO']/a[@href='https://t.me/ExLab_registration_bot' and "
                             "contains (text(), 'Присоединиться') ]")
    # LOGO_IN_BLOG = (By.XPATH, "//img[@src='./gif/logo.gif']")
    LOGO_IN_BLOG = (By.XPATH, "//img[@alt='gif_logo']")
    INSCRIPTION_IN_BLOG = (By.XPATH, "//div[@class='sc-kgflAQ gupdxc' and contains(text(), 'Твоя возможность')]")
    ALL_INSCRIPTION_IN_BLOG = (By.XPATH, "//span[@class='sc-iIPllB iQpluR is-inview' and contains(text(), 'Получить')]")

    class TopMenu:

        ABOUT_US = (By.XPATH, "//a[@class='sc-evZas hJsxZw' and contains (text(), 'О нас')]")
        PROJECTS = (By.XPATH, "//a[@class='sc-evZas hJsxZw' and contains (text(), 'Проекты')]")
        MENTORS = (By.XPATH, "//a[@class='sc-evZas hJsxZw' and contains (text(), 'Менторы')]")
        START_UP = (By.XPATH, "//a[@href='#startup'][@class='sc-evZas hJsxZw']")

    class EnterMenu:
        IN_ABOUT_US = (By.XPATH, "//div[@class='sc-eCYdqJ koNCEH is-inview' and contains (text(), 'О нас')]")
        IN_PROJECTS = (By.XPATH, "//div[@class='sc-eCYdqJ koNCEH' and contains (text(), 'Проекты')]")
        IN_MENTORS = (By.XPATH, "//div[@id='mentors']/div[@class='sc-eCYdqJ koNCEH is-inview' and contains (text(), 'Менторы')]")
        IN_STARTUP = (By.XPATH, "//div[@class='sc-eCYdqJ koNCEH is-inview' and contains(text(), 'StartUp для')]")

    class Block:
        TEXT_IN_BLOCK_ABOUT_US = (By.LINK_TEXT, "Мы стартовали в апреле 2022 года")
