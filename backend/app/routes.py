from flask import Blueprint, request, jsonify
from .models import UserInfo
from . import db

main = Blueprint('main', __name__)

@main.route('/api/user', methods=['POST'])
def add_user():
    data = request.get_json()
    user = UserInfo(name=data['name'], family=data['family'], age=data['age'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201


@main.route('/api/user', methods=['GET'])
def get_users():
    users = UserInfo.query.all()
    return jsonify([
        {"id": u.id, "name": u.name, "family": u.family, "age": u.age}
        for u in users
    ])
