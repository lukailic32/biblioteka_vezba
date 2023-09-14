from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BookSearchForm(FlaskForm):
    book_title = StringField('Book title', validators=[DataRequired()])
    submit = SubmitField('Search')