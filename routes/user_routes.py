from flask import Blueprint, request, jsonify
from handlers.user_handler import get_users, get_user_by_id, create_user, update_user, delete_user

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_all_users():
    users = get_users()
    return jsonify(users)

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@user_routes.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'name' not in data or 'email' not in data:
        return jsonify({"message": "Name and email are required"}), 400

    user = create_user(data['name'], data['email'])
    return jsonify(user), 201

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    if 'name' not in data or 'email' not in data:
        return jsonify({"message": "Name and email are required"}), 400

    user = update_user(user_id, data['name'], data['email'])
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    if delete_user(user_id):
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404
