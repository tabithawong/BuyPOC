from flask import Flask, render_template, flash

from forms import SubmitBusinessForm

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', title="Home")


@app.route('/about', methods=["GET"])
def about_us():
    return render_template("about.html", title="About Us")


@app.route('/newbusiness', methods=["GET", "POST"])
def submit_business():
    form = SubmitBusinessForm()
    if form.validate_on_submit():
        flash("New Business Submitted!")
    return render_template("submitbusiness.html", title="Submit a New Business", form=form)


if __name__ == '__main__':
    app.run()
