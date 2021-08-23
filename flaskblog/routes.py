from flask import (
    render_template,
    url_for,
    flash,
    redirect
)

from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Taylor Swift',
        'title': 'Blog post',
        'content': 'Post content',
        'date_posted': 'June 5, 2021'
    },
    {
        'author': 'Lewis Capaldi',
        'title': 'Blog post 2',
        'content': 'Post content 2',
        'date_posted': 'June 6, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed. Please check username and password','danger')
            
    return render_template('login.html', title='Login', form=form)
