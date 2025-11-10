# -*- coding: utf-8 -*-

"""
response_builder.py
--------------------
Genera respuestas basadas en las intenciones detectadas por el clasificador.
Mantiene una estructura de Clean Architecture -> Capa de servicios.
"""

import random
from app.data.repository import Repository


class ResponseBuilder:

    def __init__(self):
        self.repo = Repository()

        # Respuestas variadas para diferentes situaciones
        self.respuestas_saludo = [
            "¡Hola! 👋 Soy ToliGuide. ¿Buscas turismo, hoteles o restaurantes?",
            "¡Hey! Bienvenido a ToliGuide 😊 ¿Qué deseas conocer de Ibagué?",
            "Hola 👋 ¿Qué información necesitas hoy sobre Ibagué?"
        ]

        self.respuestas_despedida = [
            "¡Hasta luego! 👋 Que tengas un buen día.",
            "Fue un gusto ayudarte 😊 ¡Vuelve pronto!",
            "Chao chao ✌️ ¡Espero haberte ayudado!"
        ]

        self.respuestas_agradecimiento = [
            "¡Con gusto! 😊 ¿Necesitas algo más?",
            "Para eso estoy 😄 Si necesitas más info, solo dilo.",
            "Siempre un placer ayudarte 🙌"
        ]

    # ------------------------------------------------------------
    # MÉTODO PRINCIPAL
    # ------------------------------------------------------------
    def build(self, intent):
        """
        Recibe una intención y construye la respuesta correspondiente.
        """
        if intent == "saludo":
            return random.choice(self.respuestas_saludo)

        if intent == "despedida":
            return random.choice(self.respuestas_despedida)

        if intent == "agradecimiento":
            return random.choice(self.respuestas_agradecimiento)

        if intent == "pregunta_frecuente":
            return self._respuesta_pregunta()

        if intent == "turismo":
            return self._respuesta_turismo()

        if intent == "hoteles":
            return self._respuesta_hoteles()

        if intent == "restaurantes":
            return self._respuesta_restaurantes()

        if intent == "lugar_turistico":
            return self._respuesta_lugar_especifico()

        if intent == "hotel_especifico":
            return self._respuesta_hotel_especifico()

        if intent == "restaurante_especifico":
            return self._respuesta_restaurante_especifico()

        # Si no se reconoce la intención → fallback
        return None

    # ------------------------------------------------------------
    # RESPUESTAS ESPECÍFICAS
    # ------------------------------------------------------------

    # ✅ Preguntas frecuentes
    def _respuesta_pregunta(self):
        return (
            "Puedo darte información sobre precios, horarios, clima, transporte o cómo llegar. "
            "Indica un lugar o tema específico 😊"
        )

    # ✅ Turismo general
    def _respuesta_turismo(self):
        categorias = self.repo.get_turismo_categorias()
        texto = "🏞 *Lugares turísticos por categorías:*\n"

        for categoria, lugares in categorias.items():
            emoji = "📜" if categoria == "historia" else "🌿" if categoria == "naturaleza" else "🎭"
            texto += f"\n{emoji} *{categoria.capitalize()}*\n"
            for lugar in lugares.keys():
                texto += f"• {lugar}\n"

        return texto

    # ✅ Hoteles generales
    def _respuesta_hoteles(self):
        listado = self.repo.get_lista_hoteles()
        texto = "🛌 *Hoteles recomendados en Ibagué:*\n\n"
        for hotel in listado:
            texto += f"• {hotel}\n"
        texto += "\n¿Deseas información específica de uno?"
        return texto

    # ✅ Restaurantes generales
    def _respuesta_restaurantes(self):
        lista = self.repo.get_lista_restaurantes()
        texto = "🍽 *Restaurantes destacados en Ibagué:*\n\n"
        for r in lista:
            texto += f"• {r}\n"
        texto += "\n¿Te interesa uno en particular?"
        return texto

    # ✅ Lugar turístico específico
    def _respuesta_lugar_especifico(self):
        # Para obtener este lugar, se necesita que el intent_classifier ya lo detectó por nombre
        # Así que buscamos qué lugar coincide
        return self._buscar_respuesta_especifica("turismo")

    # ✅ Hotel específico
    def _respuesta_hotel_especifico(self):
        return self._buscar_respuesta_especifica("hoteles")

    # ✅ Restaurante específico
    def _respuesta_restaurante_especifico(self):
        return self._buscar_respuesta_especifica("restaurantes")

    # ------------------------------------------------------------
    # AUXILIAR QUE BUSCA INFO DEL NOMBRADO
    # ------------------------------------------------------------
    def _buscar_respuesta_especifica(self, tipo):
        """
        Busca información en el repositorio según nombre parcial.
        Prioriza coincidencia parcial.
        """
        # obtener el último mensaje del usuario
        # (esto requiere session_manager, por ahora lo traemos directamente de repo)
        # para mejorar esto, en siguientes versiones lo conectamos a session_manager
        # Aquí hacemos una búsqueda flexible
        if tipo == "turismo":
            coincidencia = self.repo.buscar_en_turismo(self._get_last_user_message())
            if coincidencia:
                desc = self.repo.get_info_lugar_turistico(coincidencia)
                return self._formato_respuesta(coincidencia, desc)

        if tipo == "hoteles":
            coincidencia = self.repo.buscar_en_hoteles(self._get_last_user_message())
            if coincidencia:
                desc = self.repo.get_info_hotel(coincidencia)
                return self._formato_respuesta(coincidencia, desc)

        if tipo == "restaurantes":
            coincidencia = self.repo.buscar_en_restaurantes(self._get_last_user_message())
            if coincidencia:
                desc = self.repo.get_info_restaurante(coincidencia)
                return self._formato_respuesta(coincidencia, desc)

        return "No encontré información específica. ¿Puedes repetir el nombre?"

    # ------------------------------------------------------------
    # FORMATO ESTÁNDAR PARA RESPUESTAS DETALLADAS
    # ------------------------------------------------------------
    def _formato_respuesta(self, nombre, descripcion):
        return f"""✅ **{nombre.title()}**
{descripcion}

📍 *Ver en Google Maps:*  
https://www.google.com/maps/search/{nombre.replace(" ", "+")}
"""

    # ------------------------------------------------------------
    # MÉTODO TEMPORAL PARA DEMO (mejorar con session_manager)
    # ------------------------------------------------------------
    def _get_last_user_message(self):
        """
        Este método es temporal para el MVP.
        En producción debe integrarse con session_manager.
        """
        # Como aún no integramos memory, regresamos el texto vacío
        # En la integración real, debes pasar el mensaje actual desde el controller
        return ""
