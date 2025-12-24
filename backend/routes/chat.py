from flask import Blueprint, request, jsonify
from services.groq_service import ask_groq

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message required"}), 400

    messages = [
        {"role": "system", "content": "You are CAMPUS GPT, a helpful campus assistant for students."},
        {"role": "user", "content": user_message}
    ]

    reply = ask_groq(messages)

    return jsonify({"reply": reply})
