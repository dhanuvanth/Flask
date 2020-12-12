from flask import Flask,redirect,url_for
app = Flask(__name__)

# url link
@app.route('/')
# fn
def hello_world():
    # val to print
    return 'Hello, World!'

@app.route('/<name>')
def user(name):
    return f'hello {name}'

@app.route('/admin')
def admin():
    # redirect fn
    return redirect(url_for('hello_world'))

if __name__ == "__main__":
    app.run()