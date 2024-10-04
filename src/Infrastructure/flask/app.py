from flask import Flask, render_template, url_for, redirect, flash;
from flask_login import LoginManager, login_user, logout_user, login_required, current_user;
from flask_dance.contrib.google import make_google_blueprint, google;
from application.use_cases.user_auth_with_google import AutenticateWithGoogle;
from repositories.user_repository import UserRepository;
from core.entities.user import User;
from config.settings import *;
import os;

app = Flask(__name__, static_url_path='/src/Infrastructure/services/flask/static');

app.secret_key = SECRET_KEY;

login_manager = LoginManager();
login_manager.login_view = 'login'
login_manager.init_app(app);

google_bp = make_google_blueprint(
    cliend_id = GOOGLE_CLIENT_ID,
    cliend_secret = GOOGLE_CLIENT_SECRET,
    scope=['profile', 'email']
)

app.register_blueprint(google_bp, url_prefix='/login');

user_repository = UserRepository()
auth_user_use_case = AutenticateWithGoogle(user_repository);

@login_manager.user_loader
def load_user(user_id):
    return user_repository.GetUserbyID(int(user_id));

@app.route("/login")
def login():
    return render_template("login-register.html");

app.run(debug=True);