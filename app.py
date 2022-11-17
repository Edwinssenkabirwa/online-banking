from flask import Flask, redirect,render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


db =SQLAlchemy()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///bank.db'

db.init_app(app)


class User(db.Model):
    id =db.Column(db.Integer(), primary_key=True)
    first_name=db.Column(db.String(length=30), nullable=False)
    second_name=db.Column(db.String(length=30), nullable=False)
    email=db.Column(db.String(length=30), nullable=False)
    pswd=db.Column(db.String(length=30), nullable=False)
with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/welcome_page')
def welcome_page():
    return render_template('welcome_page.html')

@app.route('/sign_up', methods=['POST','GET'])
def sign_up():
    error=None
    if request.method =='POST':
        Firstname=request.form['firstname']
        Lastname=request.form['lastname']
        Email=request.form['email']
        Passwd=request.form['password']

        for i in Firstname:
            numbers=('1','2','3','4','5','6','7','8','9','0')
            signs=('!','@','#','$','%','^','&','*')
            if i in numbers:
                error='names should not contain numbers'
            elif i in signs:
                error='names should not contain signs'
            else:
                pass

        if len('Firstname')<2:
            error='Your name must atleast contain 2 characters'
        elif len('Firstname')>20:
            error='Your name must atmost contain 20 characters'
        elif len(Passwd)<8:
            error= 'Your password must atleast have 8 characters'
        else:
             pass
        user=User(first_name=Firstname,
                  second_name=Lastname,
                  email=Email,
                  pswd=Passwd)
        
        db.session.add(user)
        db.session.commit()
    
        return redirect(url_for('user_list',id=user.id,first_name=user.first_name, email=user.email ))

    return render_template('sign_up.html', error=error)


@app.route('/login')
def login():
    
    
    return render_template('login.html')

@app.route('/user_details')
def user_list():
    
    return render_template('list.html')


if __name__=="__main__":
    app.run(debug=True)