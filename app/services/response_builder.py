class ResponseBuilder:

    def build(self, intent: str) -> str:

        if intent == "greeting":
            return "¡Hola! 😊 ¿En qué puedo ayudarte hoy?"

        if intent == "how_are_you":
            return "¡Estoy excelente! Aquí listo para ayudarte con turismo, hoteles o lo que necesites. ¿Qué deseas consultar?"

        if intent == "who_are_you":
            return "Soy ToliGuide, tu asistente turístico. Te ayudo a encontrar hoteles, restaurantes, rutas y recomendaciones sobre Tolima y Colombia. ¿Qué te gustaría saber?"

        if intent == "capabilities":
            return (
                "Puedo ayudarte con:\n"
                "✅ Información turística\n"
                "✅ Recomendación de hoteles\n"
                "✅ Restaurantes y comida típica\n"
                "✅ Lugares para visitar\n"
                "✅ Guías y tips de viaje\n\n"
                "¡Pregunta lo que necesites!"
            )

        if intent == "farewell":
            return "¡Hasta luego! 👋 Espero haber sido de ayuda. ¡Que tengas un excelente día!"

        if intent == "hotel_info":
            return "Aquí tienes recomendaciones de hoteles destacados en la zona. ¿Buscas algo económico, familiar o de lujo?"

        if intent == "food_info":
            return "¿Buscas restaurantes típicos, comida gourmet o sitios económicos? Te puedo recomendar varios en la región."

        if intent == "tourism_info":
            return "Tolima tiene lugares increíbles. ¿Quieres recomendaciones de naturaleza, aventura o cultura?"

        return None  # si no encuentra
