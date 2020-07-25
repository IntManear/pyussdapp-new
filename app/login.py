from .base_menu import Menu

class login(Menu):

    def login_sendotp(self):
        url_login_sendotp= "https://api-sandbox.onemoney.in/app/loginwithotp/send"
        Content_type = "application/json"
        organisationId = "FIN0176"
        client_id = "fp_test_9c84a33600449fa0c572dff3bae82b0ce337e2cc"
        client_secret= "cbf4cb1a14be02885e0285d737bae683d4351be745cd5e19617ca6f584b4224035cbeeb2"