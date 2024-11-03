from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, InputRequired
from spamham import spamham

# instance of flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class EmailForm(FlaskForm):
    email = TextAreaField(u'Email', render_kw={"rows": 11, "cols": 11},  validators=[InputRequired()])
    submit = SubmitField('Submit')

# home route that returns below text when root url is accessed
@app.route("/", methods=['GET', 'POST'])
def home():
    form = EmailForm()
    if form.validate_on_submit():
        return '<h1> {} </h1>'.format(spamham(form.email.data)) 
    return render_template('form.html', form=form)

if __name__ == '__main__':  
   app.run()  
