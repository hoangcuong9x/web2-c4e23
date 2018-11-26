from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/aboutmes")
def aboutmes():
    abouts = [
        {
            "title" : "Name: ",
            "aboutme" : "Hoang Cuong",
        },
        {
            "title" : "Work: ",
            "aboutme" : "o nha chan vit",
        },
        {
            "title" : "Crush: ",
            "aboutme" : "Chipu",
        },
    ]
    return render_template("about.html", aboutmes=abouts)
# school
@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)

   
# BMI
@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    bmi = weight / (height/100) ** 2
    if bmi < 16:
        cond = "Severely underweight"
    elif 16 <= bmi < 18.5:
        cond = "Underweight"
    elif 18.5 <= bmi < 25:
        cond = "Normal"
    elif 25 <= bmi < 30:
        cond = "Overweight"
    else:
        cond = "Obese"
    return render_template("bmi.html", bmi=bmi, cond=cond)

# User

@app.route("/user/<username>")
def user(username):
    users = {
        "cuong":{
            "name": "Nguyen Hoang Cuong",
            "age": 25
        },
        "minh":{
            "name": "Nguyen Bao Minh",
            "age": 21
        },
        "khoa":{
            "name": "Lam Dinh Khoa",
            "age": 18
        },
    }
    
    if username in users:
        u = users[username]
        return render_template("user.html",user = u )
    else:
        return "User not found"
if __name__ == "__main__":
    app.run(debug=True)