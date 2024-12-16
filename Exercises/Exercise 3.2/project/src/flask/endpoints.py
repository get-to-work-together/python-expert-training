from docutils.nodes import title
from flask import Flask, request, render_template, redirect, session, url_for

from ..persistence.book_persistence import *
from ..persistence.user_persistence import *

from ..models.openweathermap.get_data import get_formatted_data
from ..models.openweathermap.analyze import build_chart


app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='static')

app.secret_key = 'super secret key'


@app.route('/')
def home():
    links = {
        'Books': url_for('books'),
        'Weather': url_for('weather'),
    }
    return render_template('home.html', title = 'Home', links = links)


@app.route('/books', methods=['GET', 'POST'])
def books():
    if not session.get('username'):
        return redirect('/login?url=books')

    if request.method == 'POST':
        form_fields = request.form
        if form_fields:
            book = Book(**{field: value for field, value in form_fields.items() if field in Book.fields})
            insert_book(book)

    data = [book.to_dict() for book in select_books()]
    return render_template('books.html', title = 'Book collection', data = data)


@app.route('/books/delete', methods=['POST'])
def delete_book():
    if not session.get('username'):
        return redirect('/login?url=books')

    book_id = request.form.get('id')
    if book_id:
        delete_book_by_id(book_id)

    return redirect('/books')


@app.route('/login', methods=['GET', 'POST'])
def login():
    url = request.args.get('url', '/')
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = select_user_by_username(username)
            if user:
                valid_password = user.validate_password(password)
                if valid_password:
                    session['username'] = username
                    return redirect(url)

    return render_template('login.html', title = 'Login')


@app.route('/logout')
def logout():
    session['username'] = None
    return redirect('/login')


@app.route('/weather', methods=['GET'])
def weather():
    if not session.get('username'):
        return redirect('/login?url=weather')

    days = request.args.get('days') or 14
    city = request.args.get('city')
    if city is None or city == '':
        data = None
    else:
        data = get_formatted_data(city, days)
        build_chart(data, city = city)

    return render_template('weather.html', title = 'Weather forecast', data = data)


