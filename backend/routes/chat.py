from flask import Blueprint, request, jsonify
from services.groq_service import ask_groq
from models.user import User
from config import db
from utils.xp_rules import get_xp_for_action
from utils.gamification import calculate_level

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_id = data.get("user_id")
    user_message = data.get("message")

    if not user_id or not user_message:
        return jsonify({"error": "user_id and message required"}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    messages = [
        {
            "role": "system",
            "content": (
                "You are CAMPUS GPT, a friendly campus assistant. "
                "Speak briefly, clearly, and motivate the student like a game coach."
            )
        },
        {"role": "user", "content": user_message}
    ]

    ai_reply = ask_groq(messages)

    # 🎮 Gamification
    xp_gained = get_xp_for_action("chat")
    user.xp += xp_gained
    user.level = calculate_level(user.xp)

    db.session.commit()

    return jsonify({
        "reply": ai_reply,
        "xp_gained": xp_gained,
        "total_xp": user.xp,
        "level": user.level
    })
