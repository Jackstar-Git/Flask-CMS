from flask import render_template, request, redirect, url_for, session, Blueprint, make_response
from Models import User
from logging_utility import logger
from utility import hash_password

login_blueprint = Blueprint("login", __name__)


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = request.form.get("remember-me", type=bool)

        user: dict | None = User.find_user_by_mail(email)
        if user is None:
            error = "User not found!"
            return render_template('login.jinja-html', error=error)
        if user.get("login_tries", 0) >= 5:
            error = "This account is blocked because you entered the wrong password too many times!"
            logger.warning(msg="This account is blocked because you entered the wrong password too many times!")
            return render_template('login.jinja-html', error=error)
        if user and user['password'] == hash_password(password):
            session["user"] = user
            if remember:
                session.permanent = True
                print(session)
            User.update_user_data(user["_id"], login_tries = 0)
            return redirect(url_for('dashboard.dashboard'))
        else:
            error = "Invalid email or password!"
            logger.warning(msg="Invalid email or password!")
            if user:
                User.update_user_data(user["_id"], login_tries = user.get("login_tries", 0) +1)
            return render_template('login.jinja-html', error=error)

    return render_template('login.jinja-html')

