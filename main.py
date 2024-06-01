from flask import Flask, render_template
import os
from logging_utility import logger
from routes import blueprints
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

for route in blueprints:
    print(route)
    app.register_blueprint(route)



@app.route('/')
def home():
    return render_template('index.jinja-html')


@app.errorhandler(404)
def page_not_found(error):
    logger.info("A page was not found! %s", error)
    return render_template("404.html"), {"Refresh": f"5; url={app.url_for("home")}"}



if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
    logger.info("*"*50)
    logger.info("Application Server started!")
