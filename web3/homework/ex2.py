from flask import Flask, render_template, request
import mlab
from mlab import Newbike

mlab.connect()
ex2 = Flask(__name__)
@ex2.route("/new_bike", methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        #User request form
        return render_template("ex1.html")
    elif request.method == "POST":
        form = request.form
        print(form)
        m = form["model"]
        dlfee = form["dailyfee"]
        img = form["image"]
        y = form["year"]
        
        nbike = Newbike(model=m, dailyfee=dlfee, image=img, year=y)
        nbike.save()

        return "ahihihi"

if __name__=="__main__":
    ex2.run(debug=True)