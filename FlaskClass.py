from flask import Flask
from flask_wtf import CSRFProtect
import os

template_name = os.getenv("THEME_NAME")
app = Flask(__name__, template_folder=f'themes/{template_name}/templates', static_folder=f"themes/{template_name}/static")  
app.secret_key = os.urandom(24)
csrf = CSRFProtect(app)