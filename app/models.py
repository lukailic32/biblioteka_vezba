from app import db


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), index=True)
    pages = db.Column(db.Integer)
    title = db.Column(db.String(100), index=True)

    def __repr__(self):
        return '<Book {}>'.format(self.title)