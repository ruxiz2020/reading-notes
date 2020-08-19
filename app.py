from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/all-tags")
def alltags():
    return render_template("/all-tags/index.html")


@app.route("/all-categories")
def allcategories():
    return render_template("/all-categories/index.html")


@app.route("/all-archives")
def allarchives():
    return render_template("/all-archives/index.html")


@app.route('/<year>/<month>/<day>/<blogname>/')
def archives(year, month, day, blogname):

    pth = "/" + year + "/" + month + \
        "/" + day + "/" + blogname

    print(pth)
    return render_template(pth + "/index.html")


if __name__ == "__main__":
    app.run()
    app.debug = True
