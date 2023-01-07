from flask import Flask, request, render_template

#essa variavel recebe o parametro flask
app = Flask(__name__)

@app.route("/")
def home():
    nome = request.args.get("nome")
    return render_template("index.html", nome=nome)

app.run(debug=True)