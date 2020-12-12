from flask import Flask,redirect,url_for,render_template,request,session
from datetime import timedelta

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days = 5)
app.secret_key = "nhncdhjDHCBHOENBCJENIUNDEHBCJKASNlkaj"

# url link
@app.route('/')
# fn
def admin():
    # Make sure the folder name is templates inside will be the html file
    return render_template("index.html",content = "Dhanu", lst = ["joe","tony","jack"])

# mention methods in route
@app.route('/login',methods = ["GET","POST"])
def login():
    # requesting method
    if request.method == "POST":
        session.permanent = True
        user = request.form["key"]
        session['user'] = user
        return redirect(url_for("users"))
    else:
        if 'user' in session:
            return redirect(url_for('users'))
        return render_template("login.html")

@app.route('/user')
def users():
    if 'user' in session:
        user = session['user']
        return render_template("child.html",content = user)
    else:
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session.pop()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)