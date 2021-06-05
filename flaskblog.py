from re import X
from flask import (
    Flask,
    render_template
)

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)



