from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo, Regexp


class SignupForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            InputRequired(message="Name cannot be empty"),
            Length(min=3, max=64, message="Name must be between 3 and 64 characters.")
        ])

    email = StringField(
        "Email",
        validators=[
            InputRequired(message="Email cannot be empty"),
            Email(message="Email must be valid."),
            Length(message="Email cannot be over 128 characters.", max=128)
        ])

    password = PasswordField(
        "Password",
        validators=[
            InputRequired(message="Password cannot be empty"),
            Regexp(
                r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,64}$",
                message="Password must contain: lowercase, uppercase, number, special character (12–64).")
        ])

    password_repeat = PasswordField(
        "Repeat Password",
        validators=[
            InputRequired(message="Repeat password cannot be empty"),
            EqualTo("password", message="Passwords must match.")
        ])


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            InputRequired(message="Email cannot be empty"),
            Email(message="Email must be valid.")
        ])

    password = PasswordField(
        "Password", 
        validators=[
            InputRequired(message="Password cannot be empty")
        ])