from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    def __repr__(self):
        return (f'Author = ('
                f'id = {self.id}, '
                f'name = {self.name}, '
                f'birth_date = {self.birth_date}, '
                f'date_of_death = {self.date_of_death})')


    def __str__(self):
        return f'{self.id}. {self.name} ({self.birth_date}–{self.date_of_death})'


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    isbn = db.Column(db.String(13), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)

    author = db.relationship('Author', backref='books')