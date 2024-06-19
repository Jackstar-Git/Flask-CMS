from flask import Flask, render_template, url_for, make_response
import os
from logging_utility import logger
from routes import blueprints
from dotenv import load_dotenv
from waitress import serve
from datetime import datetime
from inspect import getmembers, isclass, isfunction
import functions


load_dotenv()

template_name = os.getenv("THEME_NAME")
app = Flask(__name__, template_folder=f'themes/{template_name}/templates', static_folder=f"themes/{template_name}/static")  
app.secret_key = os.urandom(24)

for route in blueprints:
    app.register_blueprint(route)

@app.context_processor
def utility_processor():
    methods = {name: func for name, func in getmembers(functions, lambda member: isclass(member) or isfunction(member))}
    return methods

@app.route('/')
def home():
    return render_template('index.jinja-html')

@app.route('/sitemap.xml')
def sitemap():
    pages = []
    lastmod = datetime.now().date().isoformat()

    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            url = url_for(rule.endpoint)
            pages.append({"loc": url, "lastmod": lastmod})
    response = make_response(render_template('sitemap.xml', pages=pages))
    response.headers["Content-Type"] = "application/xml"
    return response

@app.errorhandler(404)
def page_not_found(error):
    logger.info("A page was not found! %s", error)
    return render_template("404.html")

@app.errorhandler(403)
def access_denied(error):
    logger.info("A user tried to access a page he didn't have permissions to! %s", error)
    return render_template("403.html")



if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
    #serve(app, host='0.0.0.0', port=8080)
    logger.info("*"*50)
    logger.info("Application Server started!")
