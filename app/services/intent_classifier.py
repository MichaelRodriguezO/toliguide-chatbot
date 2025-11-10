# -*- coding: utf-8 -*-

"""
intent_classifier.py
--------------------
Clasifica la intención del usuario basándose en palabras clave
y reglas simples de contexto.
"""

from app.data.repository import Repository
from app.utils.normalizer import normalizar_texto


repo = Repository()


def classify_intent(texto):
    """
    Clasifica intenciones principales.
    Retorna un string con el tipo de intención detectada.
    """

    texto = normalizar_texto(texto)

    # Intento de saludo
    SALUDOS = [
        "hola", "holi", "buenas", "wenas", "hello", "hey",
        "saludos", "que mas", "como estas"
    ]

    if any(s in texto for s in SALUDOS):
        return "saludo"

    # Intento de despedida
    DESPEDIDAS = [
        "adios", "bye", "hasta luego", "nos vemos", "gracias"
    ]

    if any(d in texto for d in DESPEDIDAS):
        return "despedida"

    # Turismo
    if "turismo" in texto or "lugares" in texto or "turistico" in texto:
        return "turismo"

    # Hoteles
    if "hotel" in texto or "dormir" in texto or "alojamiento" in texto:
        return "hoteles"

    # Restaurantes
    if "restaurante" in texto or "comida" in texto or "comer" in texto:
        return "restaurantes"

    # Intentos especiales
    if "familia" in texto:
        return "familia"

    if "pareja" in texto or "romantico" in texto:
        return "pareja"

    if "mochilero" in texto or "hostal" in texto:
        return "mochilero"

    if "marisco" in texto or "carne" in texto or "pescado" in texto:
        return "gastronomia"

    # Lugar específico
    lugar, descripcion = repo.buscar_lugar(texto)
    if lugar:
        return ("lugar", lugar)

    # Si no detecta nada
    return None


