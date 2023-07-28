import time
import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.notification_page import NotificationPage
from .pages.locators import FormLocators


class TestsSirius:
    @pytest.mark.positive
    def test_register_form_positive_ui(self, browser):
        link = "https://uts.sirius.online//#/auth/register/qainternship"
        main_page = MainPage(browser, link)
        base_page = BasePage(browser, link)
        notification_page = NotificationPage(browser, browser.current_url)

        # открыть страницу с формой регистрации
        main_page.open()

        # заполнить поле Имя
        main_page.input_name(browser, base_page.random_string())

        # заполнить поле Фамилия
        main_page.input_surname(browser, base_page.random_string())

        # заполнить поле Отчество
        main_page.input_patronymic(browser, base_page.random_string())

        # заполнить поле Дата рождения
        main_page.input_birth_date(browser, base_page.random_date())
        time.sleep(1)

        # заполнить поле Электронная почта
        email = main_page.input_email(browser, base_page.random_fake_email())

        # заполнить поле Профессия
        main_page.input_profession(browser, base_page.random_string())

        # выбрать 1 вариант из дропдауна Страна
        main_page.choose_country(browser)

        # заполнить поле Город
        main_page.input_city(browser, base_page.random_string())

        # заполнить поле Название организации
        main_page.input_organisation(browser, base_page.random_string())

        # заполнить поле Школа
        main_page.input_school(browser, base_page.random_string())

        # заполнить поле Класс
        main_page.input_grade(browser, base_page.random_string())

        # заполнить поле ВОШ-логин
        main_page.input_vosh_login(browser, "v00.000.000")

        # заполнить поле Телефон
        main_page.input_phone(browser, base_page.random_phone(11))

        # заполнить поле СНИЛС
        main_page.input_snils(browser, 92392346925)

        # выбрать вариант олимпиады
        main_page.select_additional_olympiad(browser)

        # отметить чек-бокс "Я подтверждаю правильность указанных данных"
        main_page.check_confirm_input_data_checkbox(browser)

        # отметить чек-бокс "Я принимаю пользовательское соглашение и даю согласие на обработку персональных данных"
        main_page.check_user_agreement_checkbox(browser)

        # отметить чек-бокс "Я прочитал правила проведения"
        main_page.check_rules_checkbox(browser)

        # нажать на кнопку "Перейти к тестированию"
        main_page.click_to_testing_button(browser)

        # проверить совпадение емейла
        notification_page.check_email(browser, email)

        # нажать на кнопку “Назад”
        notification_page.back_to_register_page(browser)

    @pytest.mark.negative
    def test_register_form_negative(self, browser):
        link = "https://uts.sirius.online//#/auth/register/qainternship"
        main_page = MainPage(browser, link)
        base_page = BasePage(browser, link)

        # открыть страницу с формой регистрации
        main_page.open()

        # заполнить поле Имя
        main_page.input_name(browser, base_page.random_string())

        # заполнить поле Фамилия
        main_page.input_surname(browser, base_page.random_string())

        # заполнить поле Отчество
        main_page.input_patronymic(browser, base_page.random_string())

        # заполнить поле Дата рождения
        main_page.input_birth_date(browser, base_page.random_date())
        time.sleep(1)

        # заполнить поле Электронная почта невалидными данными
        main_page.input_email(browser, base_page.random_string())

        # проверить сообщение об ошибке под полем Электронная почта
        assert 'Неверный email' in browser.find_element(*FormLocators.EMAIL_ERROR_MESSAGE).text

        # заполнить поле Профессия
        main_page.input_profession(browser, base_page.random_string())

        # выбрать 1 вариант из дропдауна Страна
        main_page.choose_country(browser)

        # заполнить поле Город
        main_page.input_city(browser, base_page.random_string())

        # заполнить поле Название организации
        main_page.input_organisation(browser, base_page.random_string())

        # заполнить поле Школа
        main_page.input_school(browser, base_page.random_string())

        # заполнить поле Класс
        main_page.input_grade(browser, base_page.random_string())

        # заполнить поле ВОШ-логин невалидными данными
        main_page.input_vosh_login(browser, 12345)

        # проверить сообщение об ошибке под полем ВОШ-логин
        assert 'Неверный ВОШ-логин. Попробуйте ещё раз' in \
               browser.find_element(*FormLocators.VOSH_LOGIN_ERROR_MESSAGE).text

        # заполнить поле Телефон
        main_page.input_phone(browser, base_page.random_phone(11))

        # заполнить поле СНИЛС - 10 символов
        main_page.input_snils(browser, 9239234692)

        # проверить сообщение об ошибке в поле поле СНИЛС
        assert 'СНИЛС должен состоять ровно из 11 цифр' in \
               browser.find_element(*FormLocators.SNILS_FIELD_ERROR_MESSAGE).text

        # очистить поле СНИЛС
        main_page.clear_snils_field(browser)

        # заполнить поле СНИЛС - 12 символов
        main_page.input_snils(browser, 923923469251)

        # проверить сообщение об ошибке в поле поле СНИЛС
        assert 'СНИЛС должен состоять ровно из 11 цифр' in \
               browser.find_element(*FormLocators.SNILS_FIELD_ERROR_MESSAGE).text

        # очистить поле СНИЛС
        main_page.clear_snils_field(browser)

        # заполнить поле СНИЛС невалидным значением
        main_page.input_snils(browser, 68560088634)

        # проверить сообщение об ошибке в поле поле СНИЛС
        assert 'Контрольная сумма СНИЛС не совпадает' in \
               browser.find_element(*FormLocators.SNILS_FIELD_ERROR_MESSAGE).text

        # очистить поле СНИЛС
        main_page.clear_snils_field(browser)

        # выбрать вариант олимпиады
        main_page.select_additional_olympiad(browser)

        # отметить чек-бокс "Я подтверждаю правильность указанных данных"
        main_page.check_confirm_input_data_checkbox(browser)

        # отметить чек-бокс "Я принимаю пользовательское соглашение и даю согласие на обработку персональных данных"
        main_page.check_user_agreement_checkbox(browser)

        # отметить чек-бокс "Я прочитал правила проведения"
        main_page.check_rules_checkbox(browser)

        # проверить, что кнопка “Перейти к тестированию” неактивна
        main_page.check_if_to_testing_button_is_active(browser)
