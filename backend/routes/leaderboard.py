from flask import Blueprint, jsonify
from models.user import User

leaderboard_bp = Blueprint("leaderboard", __name__)

@leaderboard_bp.route("/leaderboard", methods=["GET"])
def leaderboard():
    users = User.query.filter_by(is_public=True).order_by(User.xp.desc()).all()

    leaderboard_data = []
    rank = 1

    for user in users:
        leaderboard_data.append({
            "rank": rank,
            "username": user.username,
            "level": user.level,
            "xp": user.xp,
            "streak": user.streak
        })
        rank += 1

    return jsonify(leaderboard_data)
