import random
import string
import datetime
from selenium.common.exceptions import NoSuchElementException
from .locators import PageHeaderLocators


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def change_language(self):
        self.browser.find_element(*PageHeaderLocators.CHANGE_LANGUAGE_DROPDOWN).click()
        self.browser.select_dropdown_option_by_index(2).click()

    def random_phone(self, phone_length):
        return ''.join(random.SystemRandom().choice(string.digits)
                    for _ in range(phone_length))

    def random_fake_email(self):
        variable_value = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(9))
        return variable_value.lower() + "@selenium.test"

    def random_string(self):
        variable_value = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(10))
        return variable_value

    def random_date(self):
        start_date = datetime.date.today().replace(day=1, month=1).toordinal()
        end_date = datetime.date.today().toordinal()
        random_day = datetime.date.fromordinal(random.randint(start_date, end_date))

        date_with_numbers = datetime.datetime.strptime(f"{random_day}", '%Y-%m-%d').strftime('%d.%m.%Y')
        return date_with_numbers
