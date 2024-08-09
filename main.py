from flask import render_template, url_for, make_response, request
from logging_utility import logger
from routes import blueprints
from dotenv import load_dotenv
from waitress import serve
from datetime import datetime
from inspect import getmembers, isclass, isfunction
import functions
from FlaskClass import app
import os

load_dotenv()


for route in blueprints:
    app.register_blueprint(route)

@app.before_request
def query_handler():
    request.query_params = dict(request.args)


@app.context_processor
def utility_processor():
    methods: dict = {name: func for name, func in getmembers(functions, lambda member: isclass(member) or isfunction(member))}
    methods.update({"query_params": request.query_params})
    return methods

@app.route('/')
def home():
    return render_template('index.jinja-html')


#@app.route('/<path:path>', methods=['POST'])
#def handle_file_uploads():
#    if request.method =="POST":
#        if request.files:
#            today = datetime.date
#            if not os.path.exists(os.path.join())





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
    logger.info(f"A page was not found: {request.path}; {error}")
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
