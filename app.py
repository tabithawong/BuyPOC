from flask import Flask, render_template, flash
from forms import SubmitBusinessForm
import database as db

app = Flask(__name__)

app.config["SECRET_KEY"] = "tejaspoopypants9000"


@app.route('/')
def hello_world():
    return render_template('index.html', title="Home")


@app.route('/about', methods=["GET"])
def about_us():
    return render_template("about.html", title="About Us")


@app.route('/newbusiness', methods=["GET", "POST"])
def submit_business():
    form = SubmitBusinessForm()
    data = {}
    if form.validate_on_submit():
        for field in form.data.items():
            item = field[1]
            data[field[0]] = item
        db.add_store(data["name"], data["website"], data["category"], data["address"])
        flash("Your submission is under review, thank you!")
        return render_template("index.html", form=form)
    return render_template("submitbusiness.html", title="Submit a New Business", form=form)


if __name__ == '__main__':
    app.run()
