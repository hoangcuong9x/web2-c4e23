from flask import Flask, render_template

app = Flask(__name__)
# function binding
@app.route("/")
def home():
    return "hello Flask"

@app.route("/c4e")
def c4e():
    return "hello C4E, hihi,haha, lala!"

@app.route("/me")
def me():
    return "hello, my name is Cuong"
@app.route("/hi/<name>")
def hi(name):
    return "hi " + name
@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    return str(x + y)
@app.route("/posts/<int:index>")
def posts(index):
    titles = [
        "troi mua",
        "troi nang",
        "giong bao",
        "di ngu",
    ]
    t = titles[index]
    contents = [
        "o nha",
        "di choi",
        "chay thoi",
        "tat den",
    ]
    s = contents[index]
    return render_template("post.html", title=t, content=s)

@app.route("/movie")
def movie():
    return render_template("movie.html",name="songoku", image="https://genknews.genkcdn.vn/2017/photo-1-1511425238742.jpg")
@app.route("/movies")
def movies():
    movie_list = [
        {
            "title" : "mixigaming",
            "image" : "https://yt3.ggpht.com/a-/AN66SAx6jtysLF0tCiHSU68PyPo_tkpYkvdlu0ts_g=s900-mo-c-c0xffffffff-rj-k-no",
        },
        {
            "title" : "rambo",
            "image" : "https://i.ytimg.com/vi/kz-GFxY3asw/maxresdefault.jpg",
        },
        {
            "title" : "rip113",
            "image" : "https://caothu360.com/wp-content/uploads/2018/05/rip113-k-xung-ava.jpg",
        },
    ]
    return render_template("movies.html", movies=movie_list)
if __name__ == "__main__":
    app.run(debug=True)