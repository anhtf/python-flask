#
# Flask-WTF is a Flask extension that integrates the WTForms library, making form creation and validation easier in Flask applications. It provides a structured way to build forms, handle validation, and render them in HTML. In this article, we'll explore how Flask-WTF works by building a Signup form. Before diving in, let's go over its features, field types, and prerequisites.

# Some of the key features of Flask-WTF include:

# Secure Form Handling – Automatically manages CSRF protection to prevent unauthorized submissions.
# Easy Form Rendering – Supports various field types like text fields, checkboxes, and dropdowns for smooth HTML integration.
# Built-in Validation – Includes required fields, length constraints, pattern matching, and support for custom validation.
# File Uploads – Allows users to upload files through forms seamlessly.
# In Flask-WTF, forms are defined as classes that extend the FlaskForm class. Fields are declared as class variables, making form creation simple and structured.

# Common WTForms Field Types:

# StringField: Text input field for string data.
# PasswordField: Input field for password values.
# BooleanField: Checkbox for True/False selection.
# DecimalField: Input field for decimal values.
# RadioField: Group of radio buttons for single selection.
# SelectField: Dropdown list for single selection.
# TextAreaField: Multi-line text input field.
# FileField: File upload field.

# Importing Libraries..
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class MyForm(FlaskForm):
    name        = StringField('Name', validators=[InputRequired()])
    password    = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember me')
    salary      = DecimalField('Salary', validators=[InputRequired()])
    gender      = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    country     = SelectField('Country', choices=[('IN', 'India'), ('US', 'United States'),('UK', 'United Kingdom')])
    message     = TextAreaField('Message', validators=[InputRequired()])
    photo       = FileField('Photo')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        name        = form.name.data
        password    = form.password.data
        remember_me = form.remember_me.data
        salary      = form.salary.data
        gender      = form.gender.data
        country     = form.country.data
        message     = form.message.data
        photo       = form.photo.data.filename
        return f'Name: {name} <br> Password: {generate_password_hash(password)} <br> Remember me: {remember_me} <br> Salary: {salary} <br> Gender: {gender} <br> Country: {country} <br> Message: {message} <br> Photo: {photo}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()