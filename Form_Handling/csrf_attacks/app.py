from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'anhtdh'
csrf = CSRFProtect(app)

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            flash(f'Form submitted successfully! Name: {name}', 'success')
            return render_template('index.html', form=form)
        else:
            flash('Form validation failed. Please try again.', 'danger')
    return render_template('index.html', form=form)


@app.route("/unprotected", methods=['POST'])
def unprotected_form():
    name  = request.form.get('Name', '').strip()
    if not name:
        return 'Name is required!', 400
    return f'Unprotected Form submitted successfully! Name: {name}'

if __name__ == '__main__':
    app.run(debug=True)