from flask import Flask,render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/welcome_page')
def welcome_page():
    return render_template('welcome_page.html')

@app.route('/sign_up', methods=['POST','GET'])
def sign_up():
    if request.method =='POST':
        Firstname=request.form.get('firstname')
        Lastname=request.form.get('lastname')
        Email=request.form.get('email')
        Passwd=request.form.get('password')

    return render_template('sign_up.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__=="__main__":
    app.run(debug=True)