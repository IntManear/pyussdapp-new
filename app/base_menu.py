import json

from flask_redis import FlaskRedis
redis = FlaskRedis()
from flask import make_response, current_app

class menu(object):
    def __init__(self, session_id, session, user, user_response, phone_number=None, level = None):
        self.session = session
        self.session_id = session_id
        self.user = user
        self.user_response = user_response
        self.phone_number = phone_number
        self.level = level

    def execute(self):
        raise NotImplementedError

    def ussd_proceed(self,menu_text):
        menu_text = "CON {}".format(menu_text)
        response = make_response(menu_text,200)
        response.headers['Content-Type'] = "text/plain"
        return response

    def home(self):
        """serves the home menu"""
        menu_text = "Hello, welcome to Account Aggregation services,\n Choose a service\n"
        menu_text += " 1. Register\n"
        menu_text += " 2. Login\n"
        menu_text += " 3. Exit\n"
        self.session['level'] = 1
        # print the response on to the page so that our gateway can read it
        return self.ussd_proceed(menu_text)