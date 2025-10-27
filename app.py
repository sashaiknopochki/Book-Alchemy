from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import os
from datetime import datetime
from data_models import db, Author, Book


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
db.init_app(app)

"""with app.app_context():
  db.create_all()"""


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_author', methods=['GET', 'POST'])
def handle_author():
    if request.method == 'POST':
        birth_date_str = request.form["birthdate"]
        death_date_str = request.form["date_of_death"]

        author = Author(
            name=request.form["name"],
            birth_date=datetime.strptime(birth_date_str, "%Y-%m-%d").date() if birth_date_str else None,
            date_of_death=datetime.strptime(death_date_str, "%Y-%m-%d").date() if death_date_str else None
        )
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_author.html')


@app.route('/add_book', methods=['GET', 'POST'])
def handle_book():
    if request.method == 'POST':
        book = Book(
            title=request.form["title"],
            author_id=request.form["author_id"],
            isbn=request.form["isbn"],
            publication_year=request.form["publication_year"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))

    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)