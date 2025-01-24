from flask import Flask

app=Flask(__name__)

@app.route("/home",methods=["GET","POST"])
def home():
    return "<h1> Devesh </h1>"

if __name__ == "__main__":
    app.run()