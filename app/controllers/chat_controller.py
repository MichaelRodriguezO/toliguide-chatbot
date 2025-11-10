from flask import Blueprint, request, jsonify
from app.services.intent_classifier import IntentClassifier
from app.services.response_builder import ResponseBuilder
from app.services.fallback import FallbackService
from app.services.session_manager import SessionManager
from app.utils.normalizer import normalizar_texto
from app.utils.sanitizer import sanitize_text
from app.utils.validator import is_valid_message

chat_bp = Blueprint("chat", __name__)

classifier = IntentClassifier()
builder = ResponseBuilder()
fallback = FallbackService()
session_manager = SessionManager()


@chat_bp.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"response": "No se enviaron datos al servidor."}), 400

        message = data.get("message", "").strip()
        session_id = data.get("session_id", "anon-session")

        # Validación
        if not is_valid_message(message):
            return jsonify({"response": "El mensaje está vacío o no es válido."}), 400

        # Limpieza y normalización
        safe_message = sanitize_text(message)
        normalized_message = normalizar_texto(safe_message)

        # Registrar el mensaje del usuario
        session_manager.save_user_message(session_id, normalized_message)

        # Clasificar intención
        intent = classifier.classify(normalized_message)

        # Generar respuesta basada en intención
        response = builder.build(intent)

        # Si la intención no tiene respuesta
        if not response:
            response = fallback.handle(normalized_message)

        # Guardar respuesta del bot en la sesión
        session_manager.save_bot_message(session_id, response)

        return jsonify({
            "response": response,
            "session_id": session_id
        })

    except Exception as e:
        print("Error en chat_controller:", str(e))
        return jsonify({
            "response": "Ocurrió un error inesperado en el servidor. Intenta nuevamente."
        }), 500
