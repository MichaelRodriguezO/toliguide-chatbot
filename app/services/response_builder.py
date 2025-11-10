# -*- coding: utf-8 -*-

"""
response_builder.py
--------------------
Genera respuestas basadas en intenciones detectadas por el clasificador.
"""

from app.data.repository import Repository
from app.data.info_data import DATA
from app.utils.normalizer import normalizar_texto


repo = Repository()


def build_response(intent, texto_usuario, contexto=None):
    """
    Construye la respuesta dependiendo de la intención detectada.
    """

    # SALUDO
    if intent == "saludo":
        return (
            "¡Hola! 👋 Soy ToliGuide, tu asistente turístico de Ibagué 🇨🇴.\n"
            "Puedo ayudarte con:\n"
            "🏞 Turismo\n🛌 Hoteles\n🍽 Restaurantes\n"
            "¿Qué deseas saber?"
        )

    # DESPEDIDA
    if intent == "despedida":
        return "¡Hasta luego! 😊 Gracias por usar ToliGuide."

    # TURISMO (listar categorías)
    if intent == "turismo":
        categorias = DATA["turismo"]
        r = "🏞 Lugares turísticos por categoría:\n"
        for cat, lugares in categorias.items():
            emoji = {
                "historia": "📜",
                "naturaleza": "🌿",
                "cultura": "🎭",
            }.get(cat, "📍")
            r += f"\n{emoji} {cat.capitalize()}:\n• " + "\n• ".join(lugares.keys()) + "\n"
        return r

    # HOTELES
    if intent == "hoteles":
        hoteles = DATA["hoteles"]
        return "🛌 Hoteles recomendados:\n• " + "\n• ".join(hoteles.keys())

    # RESTAURANTES
    if intent == "restaurantes":
        rest = DATA["restaurantes"]
        return "🍽 Restaurantes destacados:\n• " + "\n• ".join(rest.keys())

    # FAMILIA
    if intent == "familia":
        return (
            "👨‍👩‍👧 Lugares ideales para familias:\n"
            "• Casa Morales\n• Cañón del Combeima\n• Jardín Botánico San Jorge\n• Restaurante Altavista"
        )

    # PAREJA
    if intent == "pareja":
        return (
            "💑 Ideal para parejas:\n"
            "• La Ricotta\n• Hotel Dann Combeima\n• Restaurante Altavista"
        )

    # MOCHILERO
    if intent == "mochilero":
        return (
            "🎒 Recomendado para mochileros:\n"
            "• Eco Star Hotel\n• Chorilongo\n• Parque Museo La Martinica"
        )

    # GASTRONOMIA
    if intent == "gastronomia":
        return (
            "🍤 Lugares recomendados según gastronomía:\n"
            "• Maria y el Mar (mariscos)\n"
            "• Punta del Este (mariscos)\n"
            "• La Parrilla de Marcos (carnes)\n"
            "• El Fogón Llanero (mamona tradicional)\n"
        )

    # INTENCIÓN DE LUGAR ESPECÍFICO
    if isinstance(intent, tuple) and intent[0] == "lugar":
        lugar = intent[1]
        lugar_norm = normalizar_texto(lugar)
        encontrado, descripcion = repo.buscar_lugar(lugar_norm)
        if encontrado:
            return f"📍 {encontrado}:\n{descripcion}\nVer en Google Maps:\nhttps://www.google.com/maps/search/{encontrado.replace(' ', '+')}"

    # Si llega aquí, la intención no estaba contemplada
    return "No estoy seguro de cómo ayudarte con eso. ¿Puedes darme más detalles?"
