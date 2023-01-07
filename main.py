from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

#essa variavel recebe o parametro flask
app = Flask(__name__)
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
    nome = request.args.get("nome")
    return render_template("index.html", nome=nome)

app.run(debug=True)