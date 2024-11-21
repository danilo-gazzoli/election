import sys;
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')));

from src.infrastructure.repositories.user_repository import UserRepository;
from src.adapters.user_adapter import UserAdapter;
from src.application.use_cases.user_auth_with_google import AuthenticateWithGoogle;
from src.core.entities.user import User;
from flask import Flask, render_template, url_for, redirect, flash, request;
from flask_login import LoginManager, login_user, logout_user, login_required, current_user;
from flask_dance.contrib.google import make_google_blueprint, google;
from config.settings import *;
from werkzeug.security import generate_password_hash, check_password_hash;

app = Flask(__name__, static_url_path='/src/infrastructure/services/flask/static');

app.secret_key = SECRET_KEY;

login_manager = LoginManager();
login_manager.login_view = 'login'
login_manager.init_app(app);

user_repository = UserRepository()
auth_user_use_case = AuthenticateWithGoogle(user_repository);

@login_manager.user_loader
def load_user(user_id):
    user = user_repository.GetUserbyID(int(user_id));
    if user:
        return UserAdapter(user);
    return None;

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email");
        password = request.form.get("password");

        user_list = user_repository.GetUserbyFilter(email=email);
        
        if not user_list:
            flash("Invalid email or password.", "danger");
            return redirect(url_for("login"));

        user = user_list[0];

        if check_password_hash(user.password, password):
            user.is_logged = True;
            user_repository.UpdateUser(user);
            
            login_user(UserAdapter(user));
            flash("Login successfully!", "success");
            return redirect(url_for("section_dashboard"));
        else:
            flash("Invalid email or password.", "danger");
            return redirect(url_for("login"));
    return render_template("login-register.html");
    
@app.route("/logout")
def logout():
    user = current_user.user;
    user.is_logged = False;
    user_repository.UpdateUser(user);
    logout_user();
    flash('Logout successfully!', 'success');
    return redirect(url_for('login'));


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name");
        email = request.form.get("email");
        password = request.form.get("password");

        existing_user = user_repository.GetUserbyFilter(email=email);
        if existing_user:
            flash("Email already registered.", "danger");
            return redirect(url_for("register"));
        
        password_hash = generate_password_hash(password);

        new_user = User(
            _id=None,  
            _name=name,
            _email=email,
            _password=password_hash,  # Idealmente, criptografe a senha antes de armazenar
            _is_logged=False
        );
        
        user_repository.CreateUser(new_user);
        
        login_user(new_user);
        flash("Registration successful! You are now logged in.", "success");
        return redirect(url_for("/admin/dashboard"));

    return render_template("login-register.html");

@app.route("/admin/dashboard", methods=['GET'])
def section_dashboard():
    return render_template("adm-dash.html");

@app.route("/admin/candidate")
def section_candidate():
    return render_template("candidate-form.html");

@app.route("/admin/election")
def section_election():
    return render_template("election-form.html");

@app.route("/admin/party")
def section_party():
    return render_template("party-form.html");

@app.route("/admin/users")
def section_users():
    return render_template("user-form.html");

@app.route("/")
def section_():
    return render_template("login-register.html");

app.run(debug=True);