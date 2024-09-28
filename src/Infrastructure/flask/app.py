from flask import Flask, render_template, url_for;

app = Flask(__name__, static_url_path='/src/Infrastructure/services/flask/static');

@app.route("/")
def login():
    return render_template("login-register.html");

app.run(debug=True);