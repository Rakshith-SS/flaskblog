from flask import Flask, url_for, render_template, request, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, MakePost
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "You Found out dude"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///write.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a database instance 
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    # create a column for time stamp
    title = db.Column(db.String(120), nullable = False)
    author = db.Column(db.String(50) , nullable = False)    
    content = db.Column(db.Text, nullable = False)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow) 

    def __repr__(self):
        return f"Post( '{self.title}' , '{self.author}' , '{self.date_posted}' )"

@app.route('/home')
def index():
    blogposts = Post.query.all()
    return render_template('home.html', blogposts = blogposts)


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/post', methods=['GET','Post'])
def posts():
    post = MakePost()
    if post.is_submitted():
        blogpost = Post(title = post.title.data, author = post.author.data , content = post.message.data )
        db.session.add(blogpost)
        db.session.commit()
        return redirect('/home')
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True) 
