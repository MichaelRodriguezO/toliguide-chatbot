from app.data.info_data import INFO
from app.utils.normalizer import normalize
from app.utils.sanitizer import clean_input

def generate_response(intent, text):
    text = clean_input(text)

    if intent in ["turismo", "hoteles", "restaurantes"]:
        items = INFO[intent]
        response = f"✅ Resultados en categoría {intent}:\n"
        for key in items:
            response += f"• {key}\n"
        return response

    # búsqueda por nombre
    normalized = normalize(text)

    for category in INFO:
        for key, value in INFO[category].items():
            if normalize(key) in normalized:
                return f"{key}: {value}"

    return "No encontré información relacionada, intenta nuevamente."
