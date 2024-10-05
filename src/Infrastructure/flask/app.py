import sys;
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')));

from src.infrastructure.repositories.user_repository import UserRepository;
from src.application.use_cases.user_auth_with_google import AuthenticateWithGoogle;
from src.core.entities.user import User;
from flask import Flask, render_template, url_for, redirect, flash;
from flask_login import LoginManager, login_user, logout_user, login_required, current_user;
from flask_dance.contrib.google import make_google_blueprint, google;
from config.settings import *;

app = Flask(__name__, static_url_path='/src/Infrastructure/services/flask/static');

app.secret_key = SECRET_KEY;

login_manager = LoginManager();
login_manager.login_view = 'login'
login_manager.init_app(app);

google_bp = make_google_blueprint(
    client_id = GOOGLE_CLIENT_ID,
    client_secret = GOOGLE_CLIENT_SECRET,
    scope=['profile', 'email']
)

app.register_blueprint(google_bp, url_prefix='/login');

user_repository = UserRepository()
auth_user_use_case = AuthenticateWithGoogle(user_repository);

@login_manager.user_loader
def load_user(user_id):
    return user_repository.GetUserbyID(int(user_id));

@app.route("/login")
def login():
    if not google.authorized:
        return redirect(url_for('login2'));
    
    resp = google.get('/oauth2/v2/userinfo');
    
    if not resp.ok:
        flash('Failed to get user information from Google.', 'danger');
        return redirect(url_for('lofi'));
    
    user_info = resp.json();
    
    try:
        user = auth_user_use_case(user_info);
        login_user(user);
        flash('Login successfully!', 'success')
    except Exception as e:
        flash(str(e), 'danger');
        return redirect(url_for('lofi'));
    return redirect(url_for('/'));

@app.route("/logout")
def logout():
    user = current_user;
    user.set_is_logged(False);
    user_repository.UpdateUser(user);
    logout_user();
    flash('Logout successfully!', 'success');
    return redirect(url_for('lofi'));

@app.route("/lofi")
def lofi():
    return render_template("login-register.html");

@app.route("/register")
def register():
    resp = google.get('/oauth2/v2/userinfo');
    user_info = resp.json();
    
    user = user_repository.GetUserbyFilter(user_info['email']);
    
    if user:
        flash('This user has been registered', 'danger');
        
    user = User(
            _id = None,
            _name = user_info['name'],
            _email = user_info['email'],
            _google_id = user_info['id'],
            _password = None,
            _is_logged = False
            );
        
    user_repository.CreateUser(user);
    login_user(user);
    flash('User registered and logged in!', 'success');

@app.route("/")
def main():
    return render_template("login-register.html");

app.run(debug=True);