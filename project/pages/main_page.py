from .base_page import BasePage
from selenium.common import WebDriverException
from .locators import FormLocators


class MainPage(BasePage):

    def input_name(self, browser, name):
        self.browser.find_element(*FormLocators.NAME_FIELD).send_keys(name)

    def input_surname(self, browser, input_surname):
        self.browser.find_element(*FormLocators.SURNAME_FIELD).send_keys(input_surname)

    def input_patronymic(self, browser, patronymic):
        self.browser.find_element(*FormLocators.PATRONYMIC_FIELD).send_keys(patronymic)

    def input_birth_date(self, browser, birth_date):
        self.browser.find_element(*FormLocators.BIRTH_DATE_FIELD).send_keys(birth_date)

    def input_email(self, browser, email):
        self.browser.find_element(*FormLocators.EMAIL_FIELD).send_keys(email)
        return email

    def input_profession(self, browser, input_profession):
        self.browser.find_element(*FormLocators.PROFESSION_FIELD).send_keys(input_profession)

    def choose_country(self, browser):
        self.browser.find_element(*FormLocators.COUNTRY_DROPDOWN).click()
        self.browser.find_element(*FormLocators.ABKHAZIA).click()

    def input_city(self, browser, city):
        self.browser.find_element(*FormLocators.CITY_FIELD).send_keys(city)

    def input_organisation(self, browser, organisation):
        self.browser.find_element(*FormLocators.ORGANISATION_NAME_FIELD).send_keys(organisation)

    def input_school(self, browser, school):
        self.browser.find_element(*FormLocators.SCHOOL_FIELD).send_keys(school)

    def input_grade(self, browser, grade):
        self.browser.find_element(*FormLocators.GRADE_FIELD).send_keys(grade)

    def input_vosh_login(self, browser, vosh_login):
        self.browser.find_element(*FormLocators.VOSH_LOGIN_FIELD).send_keys(vosh_login)

    def input_phone(self, browser, phone):
        self.browser.find_element(*FormLocators.PHONE_FIELD).send_keys(phone)

    def input_snils(self, browser, snils):
        self.browser.find_element(*FormLocators.SNILS_FIELD).send_keys(snils)

    def select_additional_olympiad(self, browser):
        self.browser.find_element(*FormLocators.ADDITIONAL_OLYMPIAD_RADIOBUTTON).click()

    def check_confirm_input_data_checkbox(self, browser):
        self.browser.find_element(*FormLocators.CONFIRM_INPUT_DATA_CHECKBOX).click()

    def check_user_agreement_checkbox(self, browser):
        self.browser.find_element(*FormLocators.ACCEPT_USER_AGREEMENT_CHECKBOX).click()

    def check_rules_checkbox(self, browser):
        self.browser.find_element(*FormLocators.ACCEPT_RULES_CHECKBOX).click()

    def check_if_to_testing_button_is_active(self, browser):
        try:
            self.browser.find_element(*FormLocators.TO_TESTING_BUTTON).click()
        except WebDriverException:
            pass

    def click_to_testing_button(self, browser):
        self.browser.find_element(*FormLocators.TO_TESTING_BUTTON).click()

    def clear_snils_field(self, browser):
        self.browser.find_element(*FormLocators.SNILS_FIELD).clear()
