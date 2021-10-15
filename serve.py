from flask import Flask
from flask.helpers import send_from_directory
app=Flask(__name__)
@app.route("/")
@app.route("/<fname>")
def hello(fname="index.html"):
    return send_from_directory("",fname)
if __name__=="__main__":
    app.run(host="0.0.0.0",port="8080")