from flask import Flask,render_template


app=Flask(__name__)


@app.route('/')
def Home():
    return "Welcome"

@app.route('/home1')
def Home1():
    return "Welcome1"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')


app.run()