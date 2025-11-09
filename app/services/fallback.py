class FallbackService:

    def handle(self, user_message: str) -> str:
        return (
            "Mmm… creo que no entendí bien 🤔\n"
            "Puedes intentar preguntarme algo como:\n"
            "• Hoteles\n"
            "• Restaurantes\n"
            "• Turismo\n"
            "• Actividades\n"
            "¡Estoy aquí para ayudarte!"
        )
