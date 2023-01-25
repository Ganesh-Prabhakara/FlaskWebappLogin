from Project_files import app
from flask import render_template, redirect, url_for, flash
from Project_files.forms import RegisterForm, LoginForm, AWSForm
from Project_files.Model import User, AWS_User
from Project_files import db
from flask_login import login_user, logout_user


@app.route('/')
@app.route('/home')
def home_page():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('submit_page'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/submitted', methods=['GET', 'POST'])
def submit_page():
    form = AWSForm()
    if form.validate_on_submit():
        aws_user_to_create = AWS_User(aws_username=form.aws_username.data,
                                      aws_email_address=form.aws_email_address.data)
        db.session.add(aws_user_to_create)
        db.session.commit()
        return redirect(url_for('FinalSubmit_page'))
    if form.errors != {}:  # If there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}')

    return render_template('Submitted.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash('Success! You are logged', category='success')
        return redirect(url_for('submit_page'))
    else:
        flash('Email and password did not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/finalsubmission',  methods=['POST'])
def FinalSubmit_page():
    return render_template('FinalSubmission.html')


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect("login_page")
