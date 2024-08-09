from flask import render_template, request, redirect, url_for, session, Blueprint, abort
from Models import Post, Permissions, permission_values
from logging_utility import logger

post_blueprint = Blueprint("create", __name__)



@post_blueprint.route("/posts")
def show_posts():
    return render_template("posts.jinja-html")


@post_blueprint.route("/post/<int:post_id>")
def show_post(post_id):
    posts = Post.find_post_by_id(post_id)
    if not posts:
        return abort(404)
    return f"{str(post_id)}"


