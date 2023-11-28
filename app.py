from flask import Flask,render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('prototype.html')

@app.route("/verify")
def verification():
    return render_template("verification.html")

if __name__ == "__main__":
    app.run(debug=True)