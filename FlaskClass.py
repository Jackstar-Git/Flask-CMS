from flask import Flask
import os
from datetime import timedelta

template_name = os.getenv("THEME_NAME")
app = Flask(__name__, template_folder=f'themes/{template_name}/templates', static_folder=f"themes/{template_name}/static")  
app.secret_key = "1"#os.urandom(24)
app.permanent_session_lifetime = timedelta(days=365)