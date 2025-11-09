from flask import Blueprint, request, jsonify
from app.services.intent_classifier import detect_intent
from app.services.response_builder import generate_response
from app.services.session_manager import get_session_id

chat_bp = Blueprint("chat_bp", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    message = data.get("message", "")
    session_id = get_session_id(data)

    intent = detect_intent(message)
    response = generate_response(intent, message)

    return jsonify({"response": response})

