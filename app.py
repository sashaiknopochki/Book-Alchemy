from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import os
from data_models import db, Author, Book


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
db.init_app(app)

with app.app_context():
  db.create_all()


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)