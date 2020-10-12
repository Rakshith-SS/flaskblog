from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import MakePost
from get_jokes import fetch_joke
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "You Found out dude"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///write.db' #will create a database in the current folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False         # don't track modifications because it will use a lot of resource

# create a database instance 
db = SQLAlchemy(app)

# a  database model(object) to create a post
class Post(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    # create a column for time stamp
    title = db.Column(db.String(120), nullable = False)
    author = db.Column(db.String(50) , nullable = False)    
    content = db.Column(db.Text, nullable = False)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow) 

    def __repr__(self):
        return f"Post( '{self.title}' , '{self.author}' , '{self.date_posted}' )"

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    joke_ = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f" {self.joke_}"

# this route(address) to the home page
# return render_template looks for home.html
# and returns the home.html page
@app.route('/home')
def home():
    blogposts = Post.query.all() # fetch records table
    return render_template('home.html', blogposts = blogposts)

# route to the about page 
@app.route('/about')
def about():
    return render_template('about.html')



# create post 
@app.route('/post', methods=['GET','Post'])
def posts():
    post = MakePost()
    if post.validate_on_submit():
        blogpost = Post(title = post.title.data, author = post.author.data , content = post.message.data )
        db.session.add(blogpost)
        db.session.commit()
        return redirect('/home')
    return render_template('post.html', post=post)



dadjoke = fetch_joke()
for joke in dadjoke:
    tell_joke = Joke(joke_ = joke)
    db.session.add(tell_joke)
    db.session.commit()



@app.route('/jokes')
def jokes():
    blogjokes = Joke.query.all()
    return render_template('joke.html', blogjokes = blogjokes)


if __name__ == '__main__':
    app.run(debug=True) 
