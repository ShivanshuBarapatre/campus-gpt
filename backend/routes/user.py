from flask import Blueprint, request, jsonify
from models.user import User
from config import db
from utils.gamification import calculate_level

user_bp = Blueprint("user", __name__)

@user_bp.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username required"}), 400

    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created", "user_id": user.id})

@user_bp.route("/user/<int:user_id>/xp", methods=["POST"])
def add_xp(user_id):
    user = User.query.get(user_id)
    xp_gain = request.json.get("xp", 0)

    user.xp += xp_gain
    user.level = calculate_level(user.xp)

    db.session.commit()

    return jsonify({
        "xp": user.xp,
        "level": user.level
    })
