from application import app
from application.forms import CreateDivisionForm, CreateBoxerForm
from flask import render_template, request, redirect, url_for
import requests
from os import getenv

backend_host = "boxers-project-backend:5000"

@app.route('/', methods=["GET"])
def home():
    divisions = requests.get(f"http://{backend_host}/get/allDivisions").json()["divisions"]
    return render_template("index.html", title="Home", divisions=divisions)

@app.route('/create/division', methods=["GET", "POST"])
def create_division():
    form = CreateDivisionForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/division",
            json={
                "name": form.name.data,
                "weight_range": form.weight_range.data,
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_division.html", title="Add Division", form=form)

@app.route('/create/boxer', methods=['GET', 'POST'])
def create_boxer():
    form = CreateBoxerForm()

    json = requests.get(f"http://{backend_host}/get/allDivisions").json()
    for division in json["divisions"]:
        form.division.choices.append((division["id"], division["name"]))

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/boxer/{form.division.data}",
            json={
                "name": form.name.data,
                "weight": form.weight.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_boxer.html", title="Add Boxer", form=form)


@app.route('/read/allDivisions')
def read_divisions():
    all_divisions = Divisions.query.all()
    divisions_dict = {"divisions": []}
    for division in all_divisions:
        divisions_dict["division"].append(
            {
                "id": division.id,
                "name": division.name,
                "weight_range": division.weight_range
            }
        )
    return jsonify(boxers_dict)


@app.route('/read/allBoxers')
def read_boxers():
    all_boxers = Boxers.query.all()
    boxers_dict = {"boxers": []}
    for boxer in all_boxers:
        boxers_dict["boxers"].append(
            {
                "id": boxer.id,
                "name": boxer.name,
                "weight": boxer.weight
            }
        )
    return jsonify(boxers_dict)

@app.route('/update/division/<int:id>', methods=['GET','POST'])
def update_division(id):
    form = DivisionForm()
    division = Divisions.query.get(id)

    if request.method == "POST":
        division.name = form.name.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_division.html', division=division, form=form)


@app.route('/update/boxer/<int:id>', methods=['GET','POST'])
def update_boxer(id):
    form = BoxerForm()
    boxer = Boxers.query.get(id)

    if request.method == "POST":
        boxer.name = form.name.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_boxer.html', boxer=boxer, form=form)

@app.route('/delete/division/<int:id>')
def delete_division(id):
    division = Divisions.query.get(id)
    db.session.delete(division)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete/boxer/<int:id>')
def delete_boxer(id):
    boxer = Boxers.query.get(id)
    db.session.delete(boxer)
    db.session.commit()
    return redirect(url_for('home'))