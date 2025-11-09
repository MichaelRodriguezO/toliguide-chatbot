from flask import Blueprint, request, jsonify
from app.services.intent_classifier import detect_intent
from app.services.response_builder import build_response
from app.services.session_manager import get_session_id

chat_bp = Blueprint("chat_bp", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "")
    session_id = get_session_id(data)

    # Procesar intención
    intent = detect_intent(user_message)
    response = build_response(intent, user_message)

    return jsonify({"response": response, "session_id": session_id})
