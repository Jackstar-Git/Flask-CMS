from flask import Blueprint, request, send_file
from logging_utility import logger
from Models import User
import os
from FlaskClass import app

internal_blueprint = Blueprint("internal", __name__, template_folder='./templates', root_path="/")


#@internal_blueprint.before_app_request
#def before_request():
#    pass
#
@internal_blueprint.route('/uploads/<path:name>')
def uploads(name):
    print(os.path.join(app.root_path, "uploads"))
    return send_file(os.path.join(app.root_path, "uploads", name))
#
#
#
#@internal_blueprint.route('/internal/api/users')
#def get_users():
#    query = request.args.get('query', '').lower().strip()
#    results = User.find_users_by_name(query)
#    print(results)
#    return jsonify(results)



