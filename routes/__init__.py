from routes.dashboard import dashboard_blueprint
from routes.login import login_blueprint
from routes.register import register_blueprint
from routes.posts import post_blueprint
from routes.admin import admin_blueprint


blueprints = [dashboard_blueprint, login_blueprint, register_blueprint, post_blueprint, admin_blueprint]
__all__ = ["blueprints"]





