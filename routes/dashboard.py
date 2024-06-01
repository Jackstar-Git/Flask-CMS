from flask import render_template, redirect, url_for, session, Blueprint
from logging_utility import logger
from Models import User

dashboard_blueprint = Blueprint("dashboard", __name__, template_folder='./templates')


@dashboard_blueprint.route('/dashboard')
def dashboard():
    if 'email' in session:
        return render_template('dashboard.jinja-html', email=session['email'])
    else:
        return redirect(url_for('login.login'))


@dashboard_blueprint.route('/logout')
def logout():
    mail = session["email"]
    session.pop('email', None)
    logger.info("User %s successfully logged out.", mail)
    return redirect(url_for('home'))


@dashboard_blueprint.route("/delete")
def delete():
    mail = session["email"]
    session.pop("email", None)
    logger.info("User %s successfully deleted their account.", mail)
    user = User.find_user_by_mail(mail)
    User.delete_user(user["_id"])
    return redirect(url_for('home'))
