from flask import render_template, redirect, url_for, session, Blueprint,abort
from logging_utility import logger
from Models import User

dashboard_blueprint = Blueprint("dashboard", __name__, template_folder='./templates')


@dashboard_blueprint.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.jinja-html', user=session["user"])
    else:
        return redirect(url_for('login.login'))


@dashboard_blueprint.route('/logout')
def logout():
    mail = session["user"]["email"]
    session.clear()
    logger.info("User %s successfully logged out.", mail)
    return redirect(url_for('home'))


@dashboard_blueprint.route("/delete_account/<int:user_id>")
def delete(user_id):
    if not session.get("user"):
        return abort(403)
    _id = session["user"]["_id"]
    if user_id != int(_id): 
        return abort(403)
    
    session.clear()
    logger.info("User %s successfully deleted their account.", _id)
    User.delete_user(user_id)
    return redirect(url_for('home'))
