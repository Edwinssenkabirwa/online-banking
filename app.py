from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///bank.db'
db =SQLAlchemy(app)


class Users(db.Model):
    id =db.Column(db.Integer(), primary_key=True)
    first_name=db.Column(db.String(length=30), nullable=False)
    second_name=db.Column(db.String(length=30), nullable=False)



@app.route('/')
@app.route('/welcome_page')
def welcome_page():
    return render_template('welcome_page.html')

@app.route('/sign_up', methods=['POST','GET'])
def sign_up():
    error=None
    if request.method =='POST':
        Firstname=request.form.get('firstname')
        Lastname=request.form.get('lastname')
        Email=request.form.get('email')
        Passwd=request.form.get('password')

        for i in Firstname:
            numbers=('1','2','3','4','5','6','7','8','9','0')
            signs=('!','@','#','$','%','^','&','*')
            if i in numbers:
                error='names should not contain numbers'
            elif i in signs:
                error='names should not contain signs'
            elif len('Firstname')<2:
                error='Your name must atleast contain 2 characters'
            elif len('Firstname')>20:
                error='Your name must atmost contain 20 characters'
            elif '@' not in Email:
                error='invalid email: Emails must contain "@" character'
            elif len(Passwd)<8:
                error= 'Your password must atleast have 8 characters'
            else:
                pass

    return render_template('sign_up.html', error=error)


@app.route('/login')
def login():
    
    return render_template('login.html')


if __name__=="__main__":
    app.run(debug=True)