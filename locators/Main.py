from selenium.webdriver.common.by import By


class Main:

    DARK_BACKGROUND = (By.XPATH, "//div[@class='sc-bczRLJ ckyTig']")
    WHITE_BACKGROUND = (By.XPATH, "//div[@class='sc-bczRLJ cxdoLY']")
    LOGO = (By.XPATH, "//img[@alt='gif_logo']")

    LOGO_2 = {"xpath": "//div[@class='sc-gKXOVf kORzJB']/div[@id='logo_mobile']"}

    SUN_ICON = (By.XPATH, "//div[@class='sc-fnykZs fEkGUM']")
    LANGUAGE_BUTTON = (By.XPATH, "jhghg")
    JOIN_BUTTON_NOT_CLICK = (By.XPATH, "//div[@class='sc-gKXOVf kORzJB']/div[@id='logo_mobile']")
    JOIN_BUTTON = (By.XPATH, "//div[@class='sc-hAZoDl hrEelO']/a[@href='https://t.me/ExLab_registration_bot' and "
                             "contains (text(), 'Присоединиться') ]")
    # LOGO_IN_BLOG = (By.XPATH, "//img[@src='./gif/logo.gif']")
    LOGO_IN_BLOG = (By.XPATH, "//img[@alt='gif_logo']")

    INSCRIPTION_IN_BLOG = (By.XPATH, "//div[@class='sc-kgflAQ gupdxc' and contains(text(), 'Твоя возможность:')]")

    # INSCRIPTION_ALL = (By.CSS_SELECTOR, "ol[class*='sc-ivTmOn iPWoOL']>li")
    INSCRIPTION_ALL = (By.CSS_SELECTOR, "div[class*='sc-bBrHrO lmeoyY']")
    INSCRIPTION_IN_BLOG_01 = (By.XPATH, "//li[@class='sc-cxabCf iOiPKd'][1]")
    SEND_KEY_IN_TG = (By.CSS_SELECTOR, "a[class='tgme_action_button_new shine']")

    class TopMenu:

        ABOUT_US = (By.XPATH, "//a[@class='sc-evZas hJsxZw' and contains (text(), 'О нас')]")
        PROJECTS = (By.XPATH, "//a[@class='sc-evZas hJsxZw' and contains (text(), 'Проекты')]")
        MENTORS = (By.XPATH, "//a[@class='sc-evZas hJsxZw' and contains (text(), 'Менторы')]")
        START_UP = (By.XPATH, "//a[@href='#startup'][@class='sc-evZas hJsxZw']")

    class EnterMenu:
        IN_ABOUT_US = (By.XPATH, "//div[@class='sc-himrzO bOhFlH' and @id='about']")

        IN_PROJECTS = (By.XPATH, "//div[@class='sc-gSAPjG bbCMbW' and @id='projects']")
        # IN_PROJECTS_TEXT = (By.CSS_SELECTOR, "[id='projects'] > [class='sc-eCYdqJ koNCEH']")
        IN_PROJECTS_TEXT = (By.CSS_SELECTOR, "div[id='projects'] > div.sc-eCYdqJ")

        IN_MENTORS = (By.XPATH, "//div[@class='sc-fXynhf fCBIwr' and @id='mentors']")
        IN_STARTUP = (By.XPATH, "//div[@class='sc-iNWwEs iGujvc' and @id='startup']")

    class Block:
        BLOCK_TEXT_ABOUT_US = (By.XPATH, "//div[@id='about']/div[contains(text(), 'О нас')]")
        TEXT_IN_BLOCK_ABOUT_US = (By.LINK_TEXT, "Мы стартовали в апреле 2022 года")

        # Блок Почему ExLab
        GO_TO_WHY = (By.XPATH, "//div[@class='sc-jdAMXn iDQeOI']")

        # Текст Почему ExLab
        BLOCK_TEXT_WHY_EXLAB = (By.XPATH, "//div[@class='sc-jdAMXn iDQeOI']/div[contains(text(), 'Почему ExLab?')]")
        # Текст в блоке Почему ExLab
        TEXT_IN_BLOCK_WHY_EXLAB = (By.CLASS_NAME, "sc-iAvgwm fQGFrP is-inview")

        # Кнопка Присоединиться в блоке Почему ExLab
        BTN_JOIN = (By.XPATH, "//div[@class='sc-iTONeN egXhsc']/child::*")
        # Все лого в блоке
        ALL_LOGO_IN_BLOCK = (By.CSS_SELECTOR, "img[class='sc-bBXxYQ hEflMO']")

        LOGO_EASY_HELP = (By.CSS_SELECTOR, "img[class='sc-bBXxYQ hEflMO'][alt='Easyhelp ']")

        ALL = (By.CSS_SELECTOR, "ul[class='sc-iqcoie PhsYS']")


