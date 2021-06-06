from flask import (
    Flask,
    render_template,
    url_for
)
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '008c5fb26b126840a90252e5e98c8caa'

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)



