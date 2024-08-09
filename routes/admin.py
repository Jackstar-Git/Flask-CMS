from flask import render_template, redirect, url_for, session, Blueprint,abort, request, url_for
from logging_utility import logger
from Models import Permissions, permission_values, Post
from utility import convert_markdown_to_html

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@admin_blueprint.before_request
def check_admin_permissions():
    if 'user' in session:
        perms = Permissions.get_user_permissions(session["user"]["_id"])
        if not Permissions.permission_check(perms, permission_values["admin_access"]):
            abort(403)
    else:
        return redirect(url_for("login.login"))


@admin_blueprint.route('/')
def dashboard():
    return render_template('admin/admin.jinja-html', user=session["user"])

@admin_blueprint.route('/posts/all')
def all_posts():
    perms = Permissions.get_user_permissions(session["user"]["_id"])
    if not Permissions.permission_check(perms, permission_values["view_posts"]):
        return redirect(url_for("login.login"))
    return str(request.path)


@admin_blueprint.route('/posts/create', methods=["POST", "GET"])
def create_post():
    perms = Permissions.get_user_permissions(session["user"]["_id"])
    if not Permissions.permission_check(perms, permission_values["create_posts"]):
        return redirect(url_for("login.login"))

    if request.method == 'POST':
        print(convert_markdown_to_html(request.form.get("content")))
        tags_text = request.form.get("tags")

        title = request.form.get("title")
        content = request.form.get("content")
        tags = [item.strip() for item in tags_text.split(',')]
        category = request.form.get("category")
        author = session.get("_id")

        logger.info("Successfully created a post with the following title: %s", title)
        #Post.create_post(title, author, category, content, tags)

    return render_template('admin/create-post.jinja-html')

@admin_blueprint.route('/posts/categories')
def categories():
    perms = Permissions.get_user_permissions(session["user"]["_id"])
    if not Permissions.permission_check(perms, permission_values["view_posts"]):
        return redirect(url_for("login.login"))
    return str(request.path)



