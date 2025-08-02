from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def scoreboard():
    return render_template("scoreboard.html")

if __name__ == "__main__":
    app.run(debug=True)
