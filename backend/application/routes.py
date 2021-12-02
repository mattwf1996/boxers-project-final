from application import app, db
from application.models import Division, Boxer
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/division', methods=['POST'])
def create_division():
        package = request.json
        new_division = Division(
            name = json["name"],
            weight_range = json["weight range"]
        )
        db.session.add(new_division)
        db.session.commit()
        return f"Division '{new_division.name}' added to database"


@app.route('/create/boxer/<int:division_id>', methods=["POST"])
def create_boxer(division_id):
    json = request.json
    new_boxer = Boxer(
        name = json["name"],
        division_id = division_id,
        weight = json["weight"]
    )
    db.session.add(new_boxer)
    db.session.commit()
    return f"Boxer '{new_boxer.name}' added to database"
    

@app.route('/get/allDivisions', methods=["GET"])
def get_all_divisions():
    all_divisions = Division.query.all()
    json = {"divisions": []}
    for division in all_divisionss:
        boxers = []
        for boxer in division.boxers:
            boxers.append(
                {
                    "id": boxer.id,
                    "name": boxer.name,
                    "division_id": boxer.division_id,
                    "weight": boxer.weight
                }
            )
        json["divisions"].append(
            {
                "id": division.id,
                "name": division.name,
                "weight_range": division.weight_range,
            }
        )
    return jsonify(json)

@app.route('/get/allBoxers', methods=["GET"])
def get_all_boxers():
    all_boxers = Boxer.query.all()
    json = {"boxers": []}
    for boxer in all_boxers:
        json["boxers"].append(
            {
                "id": boxer.id,
                "name": boxer.name,
                "division_id": boxer.division_id,
                "weight": boxer.weight
            }
        )
    return jsonify(json)

@app.route('/get/division/<int:id>', methods=["GET"])
def get_division(id):
    division = Division.query.get(id)
    return jsonify(
        {
            "id": division.id,
            "name": division.name,
            "weight_range": division.weight_range
        }
    )

@app.route('/get/divisions/<int:id>/boxers', methods=["GET"])
def get_boxers(id):
    boxers = Division.query.get(id).boxers
    json = {"boxers": []}
    for boxer in boxers:
        json["boxers"].append(
            {
                "id": boxer.id,
                "name": boxer.name,
                "division_id": boxer.division_id,
                "weight": boxer.weight
            }
        )
    return jsonify(json)

@app.route('/update/division/<int:id>', methods=["PUT"])
def update_division(id):
    data = request.json
    division = Division.query.get(id)
    division.name = data["name"]
    division.weight_range = data["weight_range"]
    db.session.commit()
    return f"Division '{division.name}' updated successfully"

@app.route('/delete/division/<int:id>', methods=["DELETE"])
def delete_division(id):
    division = Division.query.get(id)
    db.session.delete(division)
    return f"Division '{division.name}' deleted successfully"

@app.route('/update/boxer/<int:id>', methods=['PUT'])
def update_boxer(id):
    data = request.json
    boxer = Boxer.query.get(id)
    boxer.name = data["name"]
    boxer.weight = data["weight"]
    db.session.commit()
    return f"Boxer '{boxer.name}' updated successfully"


@app.route('/delete/boxer/<int:id>', methods=['DELETE'])
def delete_boxer(id):
    boxer = Boxer.query.get(id)
    db.session.delete(boxer)
    return f"Boxer '{boxer.name}' deleted successfully"






# @app.route('/create/boxer', methods=['POST'])
# def create_boxer():
#         package = request.json
#         new_boxer = Boxers(description=package["description"])
#         db.session.add(new_boxer)
#         db.session.commit()
#         return Response(f"Added boxer with description: {new_boxer.description}", mimetype='text/plain')

# @app.route('/read/allBoxers', methods=['GET'])
# def read_boxers():
#     all_boxers = Boxers.query.all()
#     boxers_dict = {"boxers": []}
#     for boxer in all_boxers:
#         boxers_dict["boxers"].append(
#             {
#                 "description": boxer.description,
#                 "added": boxer.added
#             }
#         )
#     return jsonify(boxers_dict)

# @app.route('/update/boxer/<int:id>', methods=['PUT'])
# def update_boxer(id):
#     package = request.json
#     boxer = Boxers.query.get(id)

#     boxer.description = package["description"]
#     db.session.commit()
#     return Response(f"Updated boxer (ID: {id}) with description: {boxer.description}", mimetype='text/plain')

# @app.route('/delete/boxer/<int:id>', methods=['DELETE'])
# def delete_boxer(id):
#     boxer = Boxers.query.get(id)
#     db.session.delete(boxer)
#     db.session.commit()
#     return Response(f"Deleted boxer with ID: {id}", mimetype='text/plain')