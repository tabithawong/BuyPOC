from flask import Flask, render_template, flash, jsonify, request
from forms import SubmitBusinessForm, FilterForm
import database as db
import time

app = Flask(__name__)
app.config["SECRET_KEY"] = "tejaspoopypants9000"

icon_images = {
    "Restaurant": "http://maps.google.com/mapfiles/ms/icons/red-dot.png",
    "Specialty Goods": "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
    "Cafe": "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
    "Apparel": "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",
    "Lifestyle": "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
}


@app.route('/', methods=["POST", "GET"])
def hello_world():
    form = FilterForm()
    data = {}
    if form.validate_on_submit():
        for field in form.data.items():
            item = field[1]
            data[field[0]] = item
        return render_template('index.html', title="Home", form=form,
                               restaurants=data["restaurants"],
                               cafes=data["cafes"],
                               apparel=data["apparel"],
                               lifestyle=data["lifestyle"],
                               specialty_goods=data["specialty_goods"]
                               )
    return render_template('index.html', title="Home", form=form, restaurants=True, cafes=True, apparel=True, lifestyle=True, specialty_goods=True)


@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    markers = []
    for c, ls in enumerate(db.get_whole()):
        coords = str(ls[4])
        lat = float(coords[0:coords.find(',')])
        lng = float(coords[coords.find(',')+2:len(coords)])
        data = {
            "category": str(ls[2]),
            "lat": lat,
            "lng": lng,
            "infobox": "<h2>" + str(ls[0]) + "</h2>" + "<a href='" + str(ls[1]) +
                       "' target='_blank'>Visit Their Website</a><p>" + str(ls[3]) + "</p>" +
                        "<p>" + str(ls[5]) + "</p>",
            "icon": icon_images[str(ls[2])]
        }
        markers.append(data)
    return jsonify({"markers": markers})


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
        db.add_store(data["name"], data["website"], data["category"], data["address"], data["country"])
        flash("Your submission is under review, thank you!")
        return render_template("index.html", form=form)
    return render_template("submitbusiness.html", title="Submit a New Business", form=form)


if __name__ == '__main__':
    app.run()
