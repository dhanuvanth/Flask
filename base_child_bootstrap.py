from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)

# url link
@app.route('/')
# fn
def hello_world():
    # Make sure the folder name is templates inside will be the html file
    return render_template("child.html")

if __name__ == '__main__':
    app.run(debug=True)