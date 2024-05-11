from flask import Blueprint, jsonify
from config.mongodb import mongo

logs = Blueprint('logs', __name__)

@logs.route('/')
def get_users():
    # Obtiene la colección de usuarios desde MongoDB
    users_collection = mongo.db.users
    # Realiza una consulta para obtener todos los usuarios
    users_list = list(users_collection.find({}, {"_id": 0}))
    # Devuelve la lista de usuarios como JSON
    return jsonify(users_list), 200