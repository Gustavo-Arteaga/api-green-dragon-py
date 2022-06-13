import os
import ast
from flask import abort
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
app.config['UPLOAD_FOLDER'] = './uploaded_files'
CORS(app)

@app.errorhandler(400)
def bad_request(e):
    return "Bad Request", 400

@app.errorhandler(404)
def page_not_found(e):
    return "URL not found", 404


@app.errorhandler(Exception)
def internal_server_error(e):
    if isinstance(e, HTTPException):
        return "Internal Server Error", 500
    return "Internal Server Error", 500




@app.route("/foo")
def index():
    return 'Decimetrix Python Backend - Green Dragon 40066 🐉'


if __name__ == '__main__':
    app.run(debug=True)
    # app.run("0.0.0.0", debug=False)
