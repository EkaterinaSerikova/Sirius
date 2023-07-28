from .base_page import BasePage
from .locators import NotificationPageLocators


class NotificationPage(BasePage):
    def check_email(self, browser, email):
        notification_text = browser.find_element(*NotificationPageLocators.EMAIL).text
        assert f'{email}' in notification_text

    def back_to_register_page(self, browser):
        self.browser.find_element(*NotificationPageLocators.BACK_BUTTON).click()
