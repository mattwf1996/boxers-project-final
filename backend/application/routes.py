from application import app, db
from application.models import Boxers
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/boxer', methods=['POST'])
def create_boxer():
        package = request.json
        new_boxer = Boxers(description=package["description"])
        db.session.add(new_boxer)
        db.session.commit()
        return Response(f"Added task with description: {new_boxer.description}", mimetype='text/plain')

@app.route('/read/allBoxers', methods=['GET'])
def read_boxers():
    all_boxers = Boxers.query.all()
    boxers_dict = {"boxers": []}
    for boxer in all_boxers:
        boxers_dict["boxers"].append(
            {
                "description": boxer.description,
                "added": task.added
            }
        )
    return jsonify(boxers_dict)

@app.route('/update/boxer/<int:id>', methods=['PUT'])
def update_boxer(id):
    package = request.json
    boxer = Tasks.query.get(id)

    boxer.description = package["description"]
    db.session.commit()
    return Response(f"Updated boxer (ID: {id}) with description: {boxer.description}", mimetype='text/plain')

@app.route('/delete/boxer/<int:id>', methods=['DELETE'])
def delete_boxer(id):
    boxer = Boxers.query.get(id)
    db.session.delete(boxer)
    db.session.commit()
    return Response(f"Deleted boxer with ID: {id}", mimetype='text/plain')