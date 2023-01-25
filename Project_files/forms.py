from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from Project_files.Model import User, AWS_User


class RegisterForm(FlaskForm):

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    email_address = StringField(label='Email ID:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class AWSForm(FlaskForm):

    def validate_aws_username(self, username_to_check):
        username = AWS_User.query.filter_by(aws_username=username_to_check.data).first()
        if username:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_aws_email_address(self, email_address_to_check2):
        email_address2 = AWS_User.query.filter_by(aws_email_address=email_address_to_check2.data).first()
        if email_address2:
            raise ValidationError('Email Address already exists! Please try a different email address')

    aws_username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    aws_email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField(label='')
    submit = SubmitField(label='Create Account')



