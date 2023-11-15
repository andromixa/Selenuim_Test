import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

main_address = "https://mail.yandex.ru"
login = "testoffftest"
passwd = "LobotomY"
letter_recipient = "andromixa@mail.ru"
letter_subject = "Good luck!"
letter_message = "Don't worry, be happy!"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    request.cls.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
