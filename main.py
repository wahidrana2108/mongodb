from flask import Flask, request, render_template, redirect, session, url_for
import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017")
db = db_client["users"]
details_table = db["details"]

app = Flask(__name__)

app.secret_key = 'no secret key'

@app.route("/registration", methods=["GET","POST"])
def registration():
    return render_template("registration.html", **locals())


if __name__ == "__main__":
    app.run(debug=True)