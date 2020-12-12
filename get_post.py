from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

# mention methods in route
@app.route('/login',methods = ["GET","POST"])
def login():
    # requesting method
    if request.method == "POST":
        user = request.form["key"]
        return redirect(url_for("hello_world",name = user))
    else:
        return render_template("login.html")

# url link
@app.route('/<name>')
# fn
def hello_world(name):
    # Make sure the folder name is templates inside will be the html file
    return render_template("child.html",content = name)

if __name__ == '__main__':
    app.run(debug=True)