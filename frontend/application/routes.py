from application import app
from application.forms import BoxerForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "boxers-project_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_boxers = requests.get(f"http://{backend_host}/read/allBoxers").json()
    return render_template('index.html', title="Home", all_boxers=all_boxers)

# @app.route('/create/boxer', methods=['GET','POST'])
# def create_boxer():
#     form = BoxerForm()

#     if request.method == "POST":
#         new_boxer = Boxers(description=form.description.data)
#         db.session.add(new_boxer)
#         db.session.commit()
#         return redirect(url_for('home'))

#     return render_template("create_boxer.html", title="Add a new Boxer", form=form)

# @app.route('/read/allBoxers')
# def read_boxers():
#     all_boxers = Boxers.query.all()
#     boxers_dict = {"boxers": []}
#     for boxer in all_boxers:
#         boxers_dict["boxers"].append(
#             {
#                 "id": boxer.id,
#                 "description": boxer.description,
#                 "completed": boxer.completed
#             }
#         )
#     return jsonify(boxers_dict)

# @app.route('/update/boxer/<int:id>', methods=['GET','POST'])
# def update_boxer(id):
#     form = BoxerForm()
#     boxer = Boxers.query.get(id)

#     if request.method == "POST":
#         boxer.description = form.description.data
#         db.session.commit()
#         return redirect(url_for('home'))

#     return render_template('update_boxer.html', boxer=boxer, form=form)

# @app.route('/delete/boxer/<int:id>')
# def delete_boxer(id):
#     boxer = Boxers.query.get(id)
#     db.session.delete(boxer)
#     db.session.commit()
#     return redirect(url_for('home'))

# @app.route('/complete/boxer/<int:id>')
# def complete_boxer(id):
#     boxer = Boxers.query.get(id)
#     boxer.completed = True
#     db.session.commit()
#     return redirect(url_for('home'))

# @app.route('/incomplete/boxer/<int:id>')
# def incomplete_boxer(id):
#     boxer = Boxers.query.get(id)
#     boxer.completed = False
#     db.session.commit()
#     return redirect(url_for('home'))