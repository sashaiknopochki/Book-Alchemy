from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import jinja2
import sqlalchemy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)