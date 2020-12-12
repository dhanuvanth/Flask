from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)

# url link
@app.route('/<name>')
# fn
def hello_world(name):
    # Make sure the folder name is templates inside will be the html file
    return render_template("index.html",content = name,lst = ["jack","tony","joe"])

if __name__ == '__main__':
    app.run(debug=True)