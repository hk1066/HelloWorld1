from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/getLogin', methods=['post'])
def login():
    uname = request.form['uname']
    pword = request.form['pass']
    print(uname, pword)
    return render_template("loggedIn.html", uname=uname, pword=pword)

@app.route('/imhere', methods=['get'])
def imhere():
    print('imhere')
    return redirect(url_for('index'), code=300)

if __name__ == '__main__':
    app.run()
