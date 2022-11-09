from distutils.log import debug
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/welcome_page')
def welcome_page():
    return render_template('welcome_page.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

if __name__=="__main__":
    app.run(debug=True)