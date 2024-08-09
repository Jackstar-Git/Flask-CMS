from flask import Blueprint, request, send_file, jsonify, redirect, abort, url_for
from werkzeug.utils import secure_filename
from logging_utility import logger
from Models import User
import os
from FlaskClass import app
from utility import convert_markdown_to_html

internal_blueprint = Blueprint("internal", __name__, template_folder='./templates', root_path="/")


@internal_blueprint.route('/uploads/<path:filename>', methods=["GET"])
def uploads(filename):
    print(os.path.join(app.root_path, "uploads"))
    return send_file(os.path.join(app.root_path, "uploads", filename))

@internal_blueprint.route('/internal/upload', methods=["POST"])
def upload_file():
    directory = request.args.get("dir", "")
    
    if 'file' not in request.files:
        return abort(400, description="No file part in the request")
    
    file = request.files['file']
    
    if file.filename == '':
        return abort(400, description="No selected file")
    
    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)
    full_file_location = os.path.join("uploads", directory, f"{name}{ext}")

    counter = 1
    while os.path.exists(full_file_location):
        filename = f"{name}_{counter}{ext}"
        full_file_location = os.path.join("uploads", directory, filename)
        counter += 1
    
    file.save(full_file_location)
    
    return str(url_for('internal.uploads', filename=filename))




@internal_blueprint.route('/internal/api/users')
def get_users():
    query = request.args.get('query', '').lower().strip()
    results = User.find_users_by_name(query)
    print(results)
    return jsonify(results)

@internal_blueprint.route("/internal/api/markdown-to-html/", methods=["POST"])
def markdown_to_html():
    return convert_markdown_to_html(request.json.get("data", ""))



