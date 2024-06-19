from flask import session

from Models import *


def get_current_user():
    return session["user"]