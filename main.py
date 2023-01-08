from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

#essa variavel recebe o parametro flask
app = Flask(__name__, template_folder="template")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sqlite3"
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    author = db.Column(db.String())


@app.route("/")
def home():
    with app.app_context():
        db.create_all()
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/post/add", methods=["POST"])
def add_post():
    try:
        form = request.form
        post = Post(title=form["title"], content=form["content"], author=form["author"])
        db.session.add(post)
        db.session.commit()
    except Exception as error:
        print("Error", error)
        
        
@app.route("/post/<id>/del", methods=["GET"])
def delete_post(id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
    except Exception as error:
        print("Error", error)
       
    
@app.route("/post/<id>/edit", methods=["POST","GET"])
def edit_post(id):
    if request.method == "POST":
        try:
            post = Post.query.get(id)
            form = request.form
            post.title = form["title"]
            post.content = form["content"]
            post.author = form["author"]
            db.session.commit()
        except Exception as error:
            print("Error", error)
            
    else:
        try:
            post = Post.query.get(id)
            return render_template("edit.html") 
        except Exception as error:
            print("Error", error)
           
    
app.run(debug=True)