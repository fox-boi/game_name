from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return test = input(yo) print(test)


@app.route('/about')
def about():
    return 'About'
