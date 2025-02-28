
from flask import Flask, render_template, redirect, url_for, request, session


app = Flask(__name__)
app.secret_key = "poiuhbsalaskcn"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listings")
def show_list():
    return render_template("listings.html")

@app.route("/details")
def show_details():
    return render_template("details.html")


if __name__ == "__main__":
    app.run(debug=True)