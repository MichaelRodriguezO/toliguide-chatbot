# -*- coding: utf-8 -*-

"""
main.py
---------------
Punto de entrada principal del proyecto ToliGuide.
Contiene:
    ✅ servidor Flask
    ✅ rutas
    ✅ integración completa con módulos del sistema
    ✅ renderizado de plantilla index.html
    ✅ manejo de sesiones
"""

import os
from flask import Flask, request, jsonify, render_template

# MÓDULOS DE LA ARQUITECTURA
from app.utils.sanitizer import sanitize_text
from app.utils.normalizer import normalizar_texto
from app.utils.validator import is_valid_message
from app.services.intent_classifier import classify_intent
from app.services.response_builder import build_response
from app.services.fallback import FallbackService
from app.services.session_manager import SessionManager


# INICIALIZAR APP
app = Flask(__name__, template_folder="app/templates")

# Gestor de sesión
session_manager = SessionManager()
fallback_service = FallbackService()


@app.route("/", methods=["GET"])
def home():
    """
    Página principal: muestra el index.html
    """
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """
    Punto de comunicación del chatbot.
    Recibe texto del usuario y devuelve respuesta generada.
    """

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"response": "No recibí ningún mensaje."})

    user_message = data["message"]

    # 1) SANITIZAR
    limpio = sanitize_text(user_message)

    # 2) NORMALIZAR
    normalizado = normalizar_texto(limpio)

    # 3) VALIDAR
    if not is_valid_message(normalizado):
        return jsonify({"response": "Perdona, no entendí tu mensaje. ¿Puedes escribirlo de otra manera?"})

    # 4) Obtener sesión previa
    session_id = request.remote_addr
    contexto = session_manager.obtener_contexto(session_id)

    # 5) CLASIFICAR INTENCIÓN
    intencion = classify_intent(normalizado)

    # 6) GENERAR RESPUESTA
    if intencion:
        respuesta = build_response(intencion, normalizado, contexto)
    else:
        respuesta = fallback_service.handle(normalizado)

    # 7) Guardar contexto
    session_manager.actualizar_contexto(session_id, normalizado, respuesta)

    return jsonify({"response": respuesta})


# 🔥 Render usa variable PORT, así se asegura que corra en producción
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"✅ Servidor iniciado en puerto {port}")
    app.run(host="0.0.0.0", port=port)
