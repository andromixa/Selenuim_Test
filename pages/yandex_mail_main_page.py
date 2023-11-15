import time
from base.base import ProtoPage, Letter


class MainPage(ProtoPage):
    # Page elements XPATHs
    enter_mail_btn = '//*[@id="header-login-button"]'
    auth_by_email_selector = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button'
    login_input = '//*[@id="passp-field-login"]'
    submit_btn = '//*[@id="passp:sign-in"]'
    pass_input = '//*[@id="passp-field-passwd"]'
    user_icon = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[1]/div/div/div[3]/div/div/a[1]/div/img'
    user_info = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[1]/div/div/div[3]/div/div/div/ul/div[1]/div/span'
    draft_folder_btn = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/nav/div[3]/div/div[1]/div/div[1]/div[9]/div/a'
    sent_folder_btn = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/nav/div[3]/div/div[1]/div/div[1]/div[6]/div/a'
    select_all_flag = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/div[2]/div/main/div[4]/div[2]/div/div[2]/div/div/div[1]/label/span'
    delete_btn = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/div[2]/div/main/div[4]/div[2]/div/div[2]/div/div/div[5]'
    to_inbox_from_draft_btn = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/nav/div[2]/div/div/div/a'
    new_letter_button = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/nav/div[2]/div/div/div/a'
    letter_to_input = '//*[@id="compose-field-1"]'
    letter_theme_input = '//*[@id="compose-field-subject-4"]'
    letter_body_input = '//*[@id="cke_1_contents"]/div/div'
    letter_close_btn = '//*[@aria-label="Закрыть"]'
    send_btn = '//*[@id="js-apps-container"]/div[2]/div[10]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/button'
    draft_folder_context = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/nav/div[3]/div/div[1]/div/div[1]/div[9]/div/a'
    draft_messages_counter = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/nav/div[3]/div/div[1]/div/div[1]/div[9]/div/div/div/span/span'
    sent_messages_counter = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/nav/div[3]/div/div[1]/div/div[1]/div[6]/div/div/div/span/span'
    sent_mesage_notif = "/div/div/div[2]/div/span"
    message = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/div[2]/div/main/div[7]/div[1]/div/div/div[3]/div/div/div/div/div/a/div/span[1]/span[2]'
    recipient_in_drafted_msg = '//*[@id="compose-field-1"]/span'
    recipient_in_sent_msg = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/div[2]/div/main/div[7]/div/div/div/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div'
    subject_in_drafted_msg = '//*[@id="compose-field-subject-4"]'
    subject_in_sent_msg = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/div[2]/div/main/div[7]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/h1/span'
    message_in_drafted_msg = '//*[@id="cke_1_contents"]/div/div'
    message_in_sent_msg = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[2]/div/div[2]/div/main/div[7]/div/div/div/div/div/div[2]/div/article/div/div'
    exit_btn = '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[1]/div/div/div[3]/div/div/div/ul/ul/li[5]/a/span'

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, login, passwd):
        self.btn_click(self.enter_mail_btn)
        self.btn_click(self.auth_by_email_selector)
        self.input_fill(self.login_input, login)
        self.btn_click(self.submit_btn)
        self.input_fill(self.pass_input, passwd)
        self.btn_click(self.submit_btn)

    def check_login(self, login):
        self.btn_click(self.user_icon)
        username = self.get_text(self.user_info).split()[0]
        assert username == login

    def draft_clean(self):
        self.btn_click(self.draft_folder_btn)
        self.btn_click(self.draft_folder_btn)
        time.sleep(2)
        self.btn_click(self.select_all_flag)
        time.sleep(2)
        if self.get_attribute(self.delete_btn, "aria-disabled") != "true":
            self.btn_click(self.delete_btn)

    def sent_clean(self):
        self.btn_click(self.sent_folder_btn)
        self.btn_click(self.sent_folder_btn)
        time.sleep(2)
        self.btn_click(self.select_all_flag)
        time.sleep(2)
        if self.get_attribute(self.delete_btn, "aria-disabled") != "true":
            self.btn_click(self.delete_btn)

    def new_letter(self):
        self.btn_click(self.new_letter_button)

    def new_letter_check(self):
        assert self.element_on_form(self.send_btn)

    def fill_in_letter(self, letter: Letter):
        self.input_fill(self.letter_to_input, letter.recipient)
        self.input_fill(self.letter_theme_input, letter.subject)
        self.input_fill(self.letter_body_input, letter.message)

    def draft_check(self):
        self.btn_click(self.letter_close_btn)
        self.page_refresh()
        draft_msg_number = self.get_text(self.draft_messages_counter)
        assert int(draft_msg_number) == 1

    def send_check(self):
        self.btn_click(self.send_btn)
        time.sleep(3)
        self.btn_click(self.sent_folder_btn)
        self.page_refresh()
        sent_msg_number = self.get_text(self.sent_messages_counter)
        assert int(sent_msg_number) == 1

    def get_drafted_msg_params(self):
        self.btn_click(self.draft_folder_btn)
        self.btn_click(self.message)
        letter = Letter(
            self.get_attribute(
                self.recipient_in_drafted_msg, "data-email"
            ),
            self.get_attribute(self.subject_in_drafted_msg, "value"),
            self.get_text(self.message_in_drafted_msg)
        )
        return letter

    def get_sent_msg_params(self):
        self.btn_click(self.sent_folder_btn)
        self.btn_click(self.message)
        letter = Letter(
            self.get_text(self.recipient_in_sent_msg),
            self.get_text(self.subject_in_sent_msg),
            self.get_text(self.message_in_sent_msg)
        )
        return letter

    def actual_vs_expected_check(self, actual_letter, expected_letter):
        assert actual_letter == expected_letter

    def exit_mail(self):
        self.btn_click(self.sent_folder_btn)
        self.btn_click(self.user_icon)
        self.btn_click(self.exit_btn)

    def exit_check(self):
        time.sleep(3)
        assert self.element_on_form(self.enter_mail_btn)
