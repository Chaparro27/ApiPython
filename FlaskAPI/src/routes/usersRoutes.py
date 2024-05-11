from flask import Blueprint, jsonify

users = Blueprint('users', __name__)

def get_users_list():
    return [
        {"id":1, "username": "Bryan"},
        {"id":2, "username": "Bryan"}
    ]

@users.route('/')
def get_users():
    return jsonify(get_users_list())

@users.route("/<user_id>", methods=["GET"])
def get_users_by_id(user_id):
    _filter = []
    try:
        _filter = [item for item in get_users_list() if item["id"] == int(user_id)]
    except ValueError:
        _filter = {"error": "Value can't be converted to int"}
    return jsonify(_filter), 200