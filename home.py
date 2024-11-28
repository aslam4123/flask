from flask import Flask,render_template,request


app=Flask(__name__)


@app.route('/')
def Home():
    return "Welcome"

@app.route('/home1')
def Home1():
    return "Welcome1"


@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')
        email=request.form.get('email')
        print(name,age,email)
    return render_template('index.html')

app.run()