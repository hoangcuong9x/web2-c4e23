from flask import Flask, render_template, request
import mlab
from movie import Movie
mlab.connect()

app = Flask(__name__)
@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "GET":
        # Uses request form
        return render_template("add_movie.html")
    elif request.method == "POST":
        form = request.form
        t = form["title"]
        img = form["image"]
        y = form["year"]
        m = Movie(title=t, image=img, year=y)
        m.save()
        return "ahihi dongok"


if __name__ == "__main__":
    app.run(debug=True)


