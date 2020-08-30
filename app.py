from flask import Flask, url_for, render_template,request,url_for,request
from forms import LoginForm, MakePost

app = Flask(__name__)
app.config['SECRET_KEY'] = "You Found out dude"

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',form = form)

@app.route('/post', methods=['GET','Post'])
def posts():
    post = MakePost()
    if post.is_submitted():
        data = request.form
        return render_template('blog.html', data = data )
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True) 
