from selene import browser, be, have, query
import pytest

@pytest.fixture
def setup_browser():
    # Установка размеров окна браузера
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser  # Передача экземпляра браузера в тесты

    browser.quit()  # Закрытие браузера после тестов

def test_google_search(setup_browser):  # Передаем фикстуру в тест
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_google_search_no_results(setup_browser):
        """Тест на отсутствие результатов поиска."""
        browser.open('https://google.com')
        browser.element('[name="q"]').should(be.blank).type('ertert34534tgdfgerg43t3').press_enter()
        # Проверка, что сообщение об отсутствии результатов отображается
        browser.element('#center_col').should(have.text('ничего не найдено'))
        print(browser.element('#center_col').get(query.text))