class IntentClassifier:

    def classify(self, text: str) -> str:
        text = text.lower()

        # Saludos
        greetings = ["hola", "buenas", "qué más", "como vamos", "hey", "holi"]
        if any(word in text for word in greetings):
            return "greeting"

        # Despedidas
        farewells = ["adiós", "chao", "hasta luego", "nos vemos", "bye", "me voy"]
        if any(word in text for word in farewells):
            return "farewell"

        # Preguntas comunes
        if "cómo estás" in text or "como estas" in text:
            return "how_are_you"

        if "quién eres" in text or "quien eres" in text:
            return "who_are_you"

        if "qué puedes hacer" in text or "que puedes hacer" in text:
            return "capabilities"

        # Dominio turístico
        if "hotel" in text:
            return "hotel_info"

        if "restaurante" in text or "restaurantes" in text:
            return "food_info"

        if "turismo" in text:
            return "tourism_info"

        # En caso contrario
        return "fallback"

