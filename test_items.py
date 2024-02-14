import time
from selenium.webdriver.common.by import By


def test_internationalization_capabilities(browser):

    # Переходим на сайт
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Визуальная проверка языка
    time.sleep(30)

    # Находим кнопку добавления в корзину
    button = browser.find_element(By.ID, "add_to_basket_form")

    # Проверка, есть ли кнопку на странице
    assert button, "Button is not found"

