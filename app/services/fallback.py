# -*- coding: utf-8 -*-

"""
fallback.py
--------------
Servicio de respaldo cuando la intención del usuario no se puede determinar.
Implementa respuestas variadas, detección básica de emociones y sugerencias.
"""

import random
from app.data.repository import Repository
from app.utils.normalizer import normalizar_texto


class FallbackService:

    def __init__(self):
        self.repository = Repository()

        # Respuestas generales cuando no entiende la intención
        self.generic_fallbacks = [
            "Perdón, no entendí bien. ¿Puedes decirlo de otra forma?",
            "Hmm... creo que no te seguí. ¿Quieres información sobre turismo, hoteles o restaurantes?",
            "Estoy aprendiendo 😅 ¿Puedes repetir la pregunta?",
            "No estoy seguro de qué necesitas. ¿Podrías aclararlo?",
            "¿Te refieres a un sitio turístico, un hotel o un restaurante?",
        ]

        # Respuestas cuando detecta frustración
        self.frustracion_respuestas = [
            "Parece que estás teniendo dificultades. Estoy aquí para ayudarte 😄",
            "No te preocupes, intentemos de nuevo. ¿Qué necesitas saber exactamente?",
            "Tranquilo, estoy contigo. Dime otra vez lo que buscas.",
        ]

        # Respuestas cuando detecta palabras de búsqueda sin lugar concreto
        self.sugerencias_orientacion = [
            "Puedo recomendarte lugares turísticos, hoteles o restaurantes. Solo dime cuál categoría buscas.",
            "¿Buscas un sitio en particular? También puedo darte recomendaciones generales.",
            "Dime si buscas información de naturaleza, cultura, historia o comida.",
        ]

        # Palabras asociadas a frustración
        self.frustracion_keywords = [
            "no funciona", "no sirve", "no entiendo", 
            "que es esto", "no ayuda", "ayuda", "wtf", "mierda",
            "huevon", "carajo", "joder", "que pasa"
        ]

        # Palabras asociadas a confusión
        self.confusion_keywords = [
            "que es", "como funciona", "no se", "explica", "apenas llego"
        ]

    # ------------------------------------------------------------
    # MÉTODOS PRINCIPALES
    # ------------------------------------------------------------

    def handle(self, mensaje):
        """
        Entrada principal del fallback.
        Decide qué tipo de respuesta usar según el contexto del mensaje.
        """
        mensaje_norm = normalizar_texto(mensaje)

        # 1. ¿Hay señales de frustración?
        if self.detect_frustracion(mensaje_norm):
            return self.respuesta_frustracion()

        # 2. ¿Está pidiendo explicación?
        if self.detect_confusion(mensaje_norm):
            return self.respuesta_orientacion()

        # 3. ¿Busca un lugar que no existe?
        sugerencia = self.buscar_sugerencia(mensaje_norm)
        if sugerencia:
            return sugerencia

        # 4. Respuesta genérica
        return self.respuesta_generica()

    # ------------------------------------------------------------
    # DETECCIÓN DE EMOCIONES BÁSICA
    # ------------------------------------------------------------

    def detect_frustracion(self, mensaje):
        return any(kw in mensaje for kw in self.frustracion_keywords)

    def detect_confusion(self, mensaje):
        return any(kw in mensaje for kw in self.confusion_keywords)

    # ------------------------------------------------------------
    # RESPUESTAS SEGÚN DETECCIÓN
    # ------------------------------------------------------------

    def respuesta_frustracion(self):
        return random.choice(self.frustracion_respuestas)

    def respuesta_orientacion(self):
        return random.choice(self.sugerencias_orientacion)

    def respuesta_generica(self):
        return random.choice(self.generic_fallbacks)

    # ------------------------------------------------------------
    # SUGERENCIAS CUANDO NO ENCUENTRA COINCIDENCIA
    # ------------------------------------------------------------

    def buscar_sugerencia(self, mensaje):
        """
        Si intenta buscar un sitio inexistente, detecta palabras claves
        y responde una sugerencia basada en categoría.
        """

        tourism_match = self.repository.buscar_en_turismo(mensaje)
        hotel_match = self.repository.buscar_en_hoteles(mensaje)
        restaurant_match = self.repository.buscar_en_restaurantes(mensaje)

        # Si no coincide con nada
        if not tourism_match and not hotel_match and not restaurant_match:
            return None

        # Si coincide parcialmente, ofrece opciones similares
        suggestions = []

        if tourism_match:
            suggestions.append(f"Tal vez buscas información sobre *{tourism_match}* 🏞.")
        if hotel_match:
            suggestions.append(f"¿Quizá te refieres a *{hotel_match}*? 🛌")
        if restaurant_match:
            suggestions.append(f"Puede que estés buscando *{restaurant_match}* 🍽.")

        if suggestions:
            return random.choice(suggestions)

        return None
