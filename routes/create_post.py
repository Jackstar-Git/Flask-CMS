from flask import render_template, request, redirect, url_for, session, Blueprint
from Models import User, Post
from logging_utility import logger
from utility import hash_password

create_post_blueprint = Blueprint("create", __name__, template_folder='./templates')


@create_post_blueprint.route('/create', methods=['GET', 'POST'])
def create_post():
    if not 'email' in session:
        return redirect(url_for("login.login"))

    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("content")
        tags = request.form.get("tags")
        category = request.form.get("category")
        author = session.get("_id")


        Post.create_post(title, author, category, content, tags)
        
        

    return render_template('create-post.jinja-html')

