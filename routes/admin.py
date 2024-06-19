from flask import render_template, redirect, url_for, session, Blueprint,abort
from logging_utility import logger
from Models import Permissions, permission_values

admin_blueprint = Blueprint("admin", __name__, template_folder='./templates')


@admin_blueprint.before_request
def check_admin_permissions():
    if 'user' in session:
        perms = Permissions.get_user_permissions(session["user"]["_id"])
        if not Permissions.permission_check(perms, permission_values["admin_access"]):
            abort(403)
    else:
        return url_for("login.login")


@admin_blueprint.route('/admin')
def dashboard():
    return render_template('admin.jinja-html', user=session["user"])


