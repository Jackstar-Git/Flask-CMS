from flask import render_template, redirect, url_for, session, Blueprint,abort, request
from logging_utility import logger
from Models import User, Permissions, permission_values

dashboard_blueprint = Blueprint("dashboard", __name__)


@dashboard_blueprint.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template("dashboard.jinja-html")
    else:
        return redirect(url_for('login.login'))


@dashboard_blueprint.route('/logout')
def logout():
    mail = session["user"]["email"]
    session.clear()
    logger.info("User %s successfully logged out.", mail)
    return redirect(url_for('home'))


@dashboard_blueprint.route("/delete_account/<int:user_id>", methods = ["DELETE"])
def delete(user_id):
    if request.method != "DELETE":
        return abort(500)
    
    if not session.get("user"):
        return abort(403)
    _id = session["user"]["_id"]
    perms = Permissions.get_user_permissions(_id)

    if user_id != int(_id) and not Permissions.permission_check(perms, permission_values["delete_users"]): 
        return abort(403)
    
    if user_id == int(_id):
        session.clear()
    

    logger.info("User %s successfully deleted their account.", _id)
    User.delete_user(user_id)
    return redirect(url_for('home'))
