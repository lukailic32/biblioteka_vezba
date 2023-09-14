from app import app
from flask import render_template, flash, redirect
from app.forms import BookSearchForm

books = [
    {
        'name': 'Book1',
        'type': 'Drama',
        'pages': '150'
    },
    {
        'name': 'Book2',
        'type': 'Roman',
        'pages': '200'
    },
    {
        'name': 'Book3',
        'type': 'Roman',
        'pages': '200'
    },
    {
        'name': 'Book4',
        'type': 'Drama',
        'pages': '130'
    },
    {
        'name': 'Book5',
        'type': 'Drama',
        'pages': '220'
    },
]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/books')
def get_books():
    return render_template('all_books.html', books=books)

@app.route('/search_book', methods=['POST', 'GET'])
def search_book():
    form = BookSearchForm()
    if form.validate_on_submit():
        flash('Searched book {}'.format(form.book_name.data))
        return redirect('/')
    return render_template('search_book.html', form=form)

@app.route('/show_book', methods=['POST'])
def show_book():
    form = BookSearchForm()
    if form.validate_on_submit():
        flash('Searched book {}'.format(form.book_name.data))
        return redirect('/')
