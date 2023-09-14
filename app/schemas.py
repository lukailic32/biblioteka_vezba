from marshmallow import Schema, EXCLUDE
from marshmallow.fields import Str, Int
from app import app


class BookRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    book_id = Int(dump_only=True)
    type = Str(required=True)
    page = Int(required=True)
    title = Str(required=True)


book_request_schema = BookRequestSchema(many=True)


@app.route('/')
def get():
    books = list()
    for i in range(0, 100):
        book = {
            'book_id': i,
            'type': 'Tip knjige',
            'page': i*10,
            'title': 'Naslov' + str(i)
        }
        books.append(book)
    return book_request_schema.dumps(books)
