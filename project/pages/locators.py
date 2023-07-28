from selenium.webdriver.common.by import By


class PageHeaderLocators:
    CHANGE_LANGUAGE_DROPDOWN = (By.CSS_SELECTOR, ".lang_switcher__dropdown-select button")
    FROM_NAME = (By.CSS_SELECTOR, ".login_page__title")


class FormLocators:

    # поля формы
    NAME_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-firstName input")
    SURNAME_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-lastName input")
    PATRONYMIC_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-patronymic input")
    BIRTH_DATE_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-birth-date input")
    EMAIL_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-email input")
    PROFESSION_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-profession input")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, ".test-locator-sf-school-country select")
    ABKHAZIA = (By.XPATH, "//option[contains(text(), 'Абхазия')]")
    CITY_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-school-city input")
    ORGANISATION_NAME_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-school-organization input")
    SCHOOL_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-school-school input")
    GRADE_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-school-grade input")
    VOSH_LOGIN_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-vosh-login-optional input")
    PHONE_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-phone input")
    SNILS_FIELD = (By.CSS_SELECTOR, ".test-locator-sf-snils-opt input")

    # ошибки полей формы
    EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, ".test-locator-sf-email .ui-schema-auth-form__error")
    VOSH_LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, ".test-locator-sf-vosh-login-optional .ui-schema-auth-form__error")
    SNILS_FIELD_ERROR_MESSAGE = (By.CSS_SELECTOR, ".test-locator-sf-snils-opt .ui-schema-auth-form__error")

    # подвал страницы
    ADDITIONAL_OLYMPIAD_RADIOBUTTON = (By.XPATH, "//ul/li[2]/span[1]")
    CONFIRM_INPUT_DATA_CHECKBOX = (By.CSS_SELECTOR, ".test-locator-sf-confirmation-of-veracity label input")
    ACCEPT_USER_AGREEMENT_CHECKBOX = (By.CSS_SELECTOR, ".test-locator-sf-users-agreement-and-personal-data label input")
    ACCEPT_RULES_CHECKBOX = (By.CSS_SELECTOR, ".test-locator-sf-familiarized-with-the-rules label input")
    TO_TESTING_BUTTON = (By.CSS_SELECTOR, "button span")


class NotificationPageLocators:
    BACK_BUTTON = (By.XPATH, "//div[2]/div/button")
    EMAIL = (By.CSS_SELECTOR, ".text-l")
