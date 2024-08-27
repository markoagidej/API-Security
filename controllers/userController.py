from flask import request, jsonify
from models.schemas.userSchema import user_schema, users_schema
from services import userService
from marshmallow import ValidationError

def save():
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    user_save = userService.save(user_data)
    return user_schema.jsonify(user_save), 201

def getAll():
    try:
        users = userService.getAll()
        return users_schema.jsonify(users), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    
def login():
    customer = request.json
    user = userService.login_customer(customer['username'], customer['password'])
    if user:
        return jsonify(user), 200
    else:
        resp = {
            "status": "Error",
            "message": "User does nto exist"
        }
        return jsonify(resp), 404