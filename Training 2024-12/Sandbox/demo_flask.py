from flask import Flask, Response
from flask import session, render_template, redirect, request, jsonify

from demo_requests import get_daily_forecasts
from user import User

app = Flask(__name__,
            static_url_path = '/',
            template_folder = 'templates',
            static_folder = 'static')

app.secret_key = 'super secret key'


@app.route('/')
def home():
    name = request.args.get('name') or 'Stranger'
    return render_template('home.html', name=name)

@app.route('/hello')
def hallo():
    name = request.args.get('name')
    return Response(f'Hallo {name}', status=200)

@app.route('/data')
def show_data():
    names = ['Klaas Jan','Janske','Steven','Maurits','Tijmen','Rene']
    return render_template('names.html', names=names)


@app.route('/api/v1/data')
def json_data():
    names = ['Klaas Jan','Janske','Steven','Maurits','Tijmen','Rene']
    return jsonify(names=names)

@app.route('/weather')
def weather():
    if session is None or 'username' not in session:
        return redirect('/login')

    city = request.args.get('city') or 'Amsterdam'
    daily_forecasts = get_daily_forecasts(city)
    return render_template('weather.html',
                           city=city,
                           daily_forecasts=daily_forecasts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session and session['username']:
        del session['username']

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if User.valid_login(username, password):
            session['username'] = username
            return redirect('/weather')

    return render_template('login.html',
                           message='Invalid username or password')


app.run()