import sys;
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')));

from src.infrastructure.repositories.user_repository import UserRepository;
from src.application.use_cases.user_auth_with_google import AuthenticateWithGoogle;
from src.core.entities.user import User;
from flask import Flask, render_template, url_for, redirect, flash, request;
from flask_login import LoginManager, login_user, logout_user, login_required, current_user;
from flask_dance.contrib.google import make_google_blueprint, google;
from config.settings import *;

app = Flask(__name__, static_url_path='/src/infrastructure/services/flask/static');

app.secret_key = SECRET_KEY;

login_manager = LoginManager();
login_manager.login_view = 'login'
login_manager.init_app(app);

user_repository = UserRepository()
auth_user_use_case = AuthenticateWithGoogle(user_repository);

@login_manager.user_loader
def load_user(user_id):
    return user_repository.GetUserbyID(int(user_id));

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = user_repository.GetUserbyFilter(email=email);
        
        if not user:
            flash("Invalid email or password.", "danger");
            return redirect(url_for("login"));

        user = user[0];

        if user.password == password:
            login_user(user);
            flash("Login successfully!", "success");
            return redirect(url_for("section_dashboard"));
        else:
            flash("Invalid email or password.", "danger");
            return redirect(url_for("login"));
    return redirect(url_for('/'));
    

@app.route("/logout")
def logout():
    user = current_user;
    user.set_is_logged(False);
    user_repository.UpdateUser(user);
    logout_user();
    flash('Logout successfully!', 'success');
    return redirect(url_for('/')); 

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Verifica se o usuário já existe
        existing_user = user_repository.GetUserbyFilter(email=email)
        if existing_user:
            flash("Email already registered.", "danger")
            return redirect(url_for("register"))

        # Cria o novo usuário
        new_user = User(
            _id=None,  # ID será gerado automaticamente
            _name=name,
            _email=email,
            _password=password,  # Idealmente, criptografe a senha antes de armazenar
            _is_logged=False
        )
        
        # Salva o usuário no banco de dados
        user_repository.CreateUser(new_user)
        
        # Realiza o login automático após o registro
        login_user(new_user)
        flash("Registration successful! You are now logged in.", "success")
        return redirect(url_for("section_dashboard"))

    return render_template("login-register.html")

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