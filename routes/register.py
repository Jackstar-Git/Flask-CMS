from flask import render_template, request, redirect, url_for, session, Blueprint
from Models import User
from logging_utility import logger
from utility import hash_password
from Models import Role


register_blueprint = Blueprint("register", __name__, template_folder='./templates')


@register_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form["email"]
        password = request.form['password']

        user = User.find_user_by_mail(email)



        if user:
            error = "Email already exists!"
            logger.warning(msg="Email already exists!")
            return render_template('register.jinja-html', error=error)

        hashed_password = hash_password(password)
        role = Role.get_by_id(1000000000000001)
        User.create_user(username, email, hashed_password, roles=[role])
        session["user"] = User.find_user_by_mail(email)
        return redirect(url_for('dashboard.dashboard'))

    return render_template('register.jinja-html')
