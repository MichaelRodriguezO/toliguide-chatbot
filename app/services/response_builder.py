from app.data.info_data import INFO
from app.utils.normalizer import normalize
from app.utils.sanitizer import clean_input

def build_map_link(name):
    import urllib.parse
    return f"📍 Ver en Google Maps: https://www.google.com/maps/search/{urllib.parse.quote(name)}"

def generate_response(intent, text):
    text = clean_input(text)
    normalized = normalize(text)

    # Mostrar categorías completas
    if intent == "turismo":
        response = "🏞 Lugares turísticos por categoría:\n"
        for category, items in INFO["turismo"].items():
            emoji = {"historia": "📜", "naturaleza": "🌿", "cultura": "🎭"}[category]
            response += f"\n{emoji} {category.capitalize()}:\n"
            for place in items:
                response += f"• {place.title()}\n"
        return response

    if intent == "hoteles":
        return "🛌 Hoteles recomendados:\n" + "\n".join([f"• {h.title()}" for h in INFO["hoteles"]])

    if intent == "restaurantes":
        return "🍽 Restaurantes destacados:\n" + "\n".join([f"• {r.title()}" for r in INFO["restaurantes"]])

    # Búsqueda por coincidencia exacta
    for category in ["turismo", "hoteles", "restaurantes"]:
        if category == "turismo":
            for subcat in INFO["turismo"].values():
                for name, desc in subcat.items():
                    if normalize(name) in normalized:
                        return f"{name.title()}:\n{desc}\n{build_map_link(name)}"
        else:
            for name, desc in INFO[category].items():
                if normalize(name) in normalized:
                    return f"{name.title()}:\n{desc}\n{build_map_link(name)}"

    # Búsqueda por palabras clave
    user_words = set(normalized.split())
    for category in ["turismo", "hoteles", "restaurantes"]:
        if category == "turismo":
            for subcat in INFO["turismo"].values():
                for name, desc in subcat.items():
                    name_words = set(normalize(name).split())
                    if user_words & name_words:
                        return f"{name.title()}:\n{desc}\n{build_map_link(name)}"
        else:
            for name, desc in INFO[category].items():
                name_words = set(normalize(name).split())
                if user_words & name_words:
                    return f"{name.title()}:\n{desc}\n{build_map_link(name)}"

    return "No entendí tu búsqueda, intenta con: turismo, hoteles o restaurantes."
