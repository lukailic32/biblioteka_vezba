from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BookSearchForm(FlaskForm):
    book_name = StringField('Book name', validators=[DataRequired()])
    submit = SubmitField('Search')