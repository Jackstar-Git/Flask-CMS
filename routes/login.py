from flask import render_template, request, redirect, url_for, session, Blueprint
from Models import User
from logging_utility import logger
from utility import hash_password

login_blueprint = Blueprint("login", __name__, template_folder='./templates')


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = request.form.get('remember')

        user = User.find_user_by_mail(email)
        print(user)
        if user and user['password'] == hash_password(password):
            session['email'] = email
            session["_id"] = user["_id"]
            if remember:
                session.permanent = True
            return redirect(url_for('dashboard.dashboard'))
        else:
            error = "Invalid email or password!"
            logger.warning(msg="Invalid email or password!")
            return render_template('login.jinja-html', error=error)

    return render_template('login.jinja-html')

