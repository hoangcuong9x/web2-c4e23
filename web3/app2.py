from flask import Flask, render_template, request
import mlab
from user import User
mlab.connect()

app2 = Flask(__name__)
@app2.route("/pass_word", methods=["GET", "POST"])
def pass_word():
    if request.method == "GET":
        # Uses request form
        return render_template("pass_word.html")
    elif request.method == "POST":
        form = request.form
        p = form["password"]
        u = form["user"]
        exist_user = User.objects(user=u).first()
        if exist_user != None:
            return 'user already exists'
        else:
            user = User(user=u, password=p)
            user.save()
            return 'lêu lêu lêu'
if __name__ == "__main__":
    app2.run(debug=True)
# flask session