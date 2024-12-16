from flask import Flask, render_template

app = Flask(__name__)

data = {'Amsterdam': '020',
        'Utrecht': '030',
        'Groningen': '050',
        'Den Haag': '070'}

@app.route('/')
def home():
    return render_template('home.html', data=data)

app.run()
