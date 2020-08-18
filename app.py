from flask import Flask, render_template
app = Flask(__name__, template_folder='.')

@app.route("/")
def index():
        #return("Index str")
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
    app.debug = True