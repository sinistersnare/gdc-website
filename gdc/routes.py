from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/ideas')
def ideas():
    return render_template("ideas.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
