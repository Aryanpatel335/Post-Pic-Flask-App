from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import RegisterForm, LoginForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import re

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
    logout_user()
    form = LoginForm()
    
    if request.method == 'POST':
        username = form.username.data
        password= form.password.data
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password_hash, password):
                flash('Logged In Successfully!', category='success')
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Credentials', category='error')
        else:
            flash('User Does Not Exist', category='error')

    return render_template("login.html", form=form, user= current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/register',methods=['GET', 'POST'])
def register():
    logout_user()
    form = RegisterForm()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if request.method == 'POST':
        email = form.email.data
        username = form.username.data
        password= form.password.data
        password2= form.password.data
        user = User.query.filter_by(username=username).first()
        email_inDB = User.query.filter_by(email=email).first()
        if user or email_inDB:
            flash('Account already exists', category='error')
        elif not re.search(regex,email):
            flash('Invalid Email', category='error')
        elif len(username) <2:
            flash('Username too short', category='error')
        elif password != password2:
            flash('Passwords do not match', category='error')
        else:
            #add user to database
            new_user = User(email=email, username=username, password_hash= generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
    return render_template("register.html", form=form, user=current_user)
    