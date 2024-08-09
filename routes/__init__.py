from flask import Blueprint
from routes.dashboard import dashboard_blueprint
from routes.login import login_blueprint
from routes.register import register_blueprint
from routes.posts import post_blueprint
from routes.admin import admin_blueprint
from routes.internal import internal_blueprint

# Collect all blueprints from globals()
blueprints = [obj for name, obj in globals().items() if isinstance(obj, Blueprint)]

__all__ = ["blueprints"]
