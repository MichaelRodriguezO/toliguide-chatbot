from app.utils.normalizer import normalize

def detect_intent(text):
    normalized = normalize(text)

    if "turismo" in normalized or "lugar" in normalized:
        return "turismo"
    if "hotel" in normalized or "dormir" in normalized:
        return "hoteles"
    if "restaurante" in normalized or "comer" in normalized:
        return "restaurantes"

    return "busqueda"

