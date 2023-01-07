from flask import Flask

#essa variavel recebe o parametro flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

app.run(debug=True)