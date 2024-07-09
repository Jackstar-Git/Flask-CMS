from flask import session

from Models import *


def get_current_user():
    return session["user"]

def load_widget(widget_id: str):
    pass

def load_content(content_id: str):
    pass
