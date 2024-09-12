from flask import Flask

app = Flask(__name__);

@app.route("/")
def Ola():
    return "<p>Olá, mundo</p>";

app.run("localhost:5000", debug=True);