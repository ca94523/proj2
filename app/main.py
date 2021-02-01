
#import sys
#from flask import Flask
#app = Flask(__name__)
#@app.route("/")
#def hello():
#    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
#    message = "Hello World from Flask in a Docker container running Python {} with Meinheld and Gunicorn (default)".format(
#        version
#    )
#    return message

import os
from app import create_app,db

app = create_app()
app.app_context().push()

@app.shell_context_processor
def make_shell_context():
    return {'db': db}
