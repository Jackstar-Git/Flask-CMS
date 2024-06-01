from routes.dashboard import dashboard_blueprint
from routes.login import login_blueprint
from routes.register import register_blueprint
from routes.create_post import create_post_blueprint


blueprints = [dashboard_blueprint, login_blueprint, register_blueprint, create_post_blueprint]
__all__ = ["blueprints"]





