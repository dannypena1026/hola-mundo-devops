from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hola Mundo - Danny Peña Adames</h1><p>Practica DevOps con Docker</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
