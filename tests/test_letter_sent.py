import pytest
from conftest import *
from pages.yandex_mail_main_page import MainPage
from base.base import Letter

letter = Letter(letter_recipient, letter_subject, letter_message)


@pytest.mark.usefixtures("browser_setup")
class TestLetterToDraft:
    def setup_class(self):
        self.driver.get(main_address)
        self.main_page = MainPage(self.driver)

    def test_login(self):
        self.main_page.login(login, passwd)
        self.main_page.check_login(login)
        # For further clearness
        self.main_page.draft_clean()
        self.main_page.sent_clean()

    def test_new_letter(self):
        self.main_page.new_letter()
        self.main_page.new_letter_check()

    def test_fill_new_letter(self):
        self.main_page.fill_in_letter(letter)
        self.main_page.send_check()

    def test_sent_vs_original(self):
        self.main_page.actual_vs_expected_check(
            self.main_page.get_sent_msg_params(), letter
        )

    def test_exit(self):
        self.main_page.exit_mail()
        self.main_page.exit_check()

    def teardown_class(self):
        self.driver.quit()
