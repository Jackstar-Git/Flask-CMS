from flask import render_template, request, redirect, url_for, session, Blueprint, abort
from Models import Post, Permissions, permission_values
from logging_utility import logger

post_blueprint = Blueprint("create", __name__, template_folder='./templates')



@post_blueprint.route("/posts")
def show_posts():
    return render_template("posts.jinja-html")


@post_blueprint.route("/post/<int:post_id>")
def show_post(post_id):
    posts = Post.find_post_by_id(post_id)
    if not posts:
        return abort(404)
    return f"{str(post_id)}"



@post_blueprint.route('/create', methods=['GET', 'POST'])
def create_post():
    if not "user" in session:
        return redirect(url_for("login.login"))
    
    perms = Permissions.get_user_permissions(session["user"]["_id"])
    if not Permissions.permission_check(perms, permission_values["create_posts"]):
        abort(403)

    if request.method == 'POST':
        tags_text = request.form.get("tags")

        title = request.form.get("title")
        content = request.form.get("content")
        tags = [item.strip() for item in tags_text.split(' ')]
        category = request.form.get("category")
        author = session.get("_id")

        logger.info("Successfully created a post with the following title: %s", title)
        Post.create_post(title, author, category, content, tags)

    return render_template('create-post.jinja-html')

