# -*- coding: utf-8 -*-

"""
intent_classifier.py
---------------------
Clasifica el mensaje del usuario en una intención específica.
Utiliza activadores definidos en el repositorio y normalización del texto.
"""

from app.data.repository import Repository
from app.utils.normalizer import normalize_text


class IntentClassifier:

    def __init__(self):
        self.repo = Repository()
        self.activadores = self.repo.get_activadores()

    # ------------------------------------------------------------
    # MÉTODO PRINCIPAL
    # ------------------------------------------------------------
    def classify(self, mensaje):
        """
        Clasifica la intención del mensaje.
        Devuelve un string que identifica la intención detectada.
        """
        mensaje = normalize_text(mensaje)

        # 1. Prioridad alta: saludo
        if self._match_intent("saludo", mensaje):
            return "saludo"

        # 2. Prioridad alta: despedida
        if self._match_intent("despedida", mensaje):
            return "despedida"

        # 3. Agradecimientos
        if self._match_intent("agradecimiento", mensaje):
            return "agradecimiento"

        # 4. Preguntas frecuentes
        if self._match_intent("preguntas", mensaje):
            return "pregunta_frecuente"

        # 5. Categorías principales
        if self._match_intent("turismo", mensaje):
            return "turismo"

        if self._match_intent("hoteles", mensaje):
            return "hoteles"

        if self._match_intent("restaurantes", mensaje):
            return "restaurantes"

        # 6. Lugar específico de turismo
        if self._buscar_lugar_turistico(mensaje):
            return "lugar_turistico"

        # 7. Hotel específico
        if self._buscar_hotel(mensaje):
            return "hotel_especifico"

        # 8. Restaurante específico
        if self._buscar_restaurante(mensaje):
            return "restaurante_especifico"

        # 9. Intención desconocida
        return "fallback"

    # ------------------------------------------------------------
    # DETECCIÓN POR PALABRAS CLAVE
    # ------------------------------------------------------------
    def _match_intent(self, intent_key, mensaje):
        """
        Revisa si alguna palabra clave del intent está en el mensaje.
        """
        palabras = self.activadores.get(intent_key, [])
        return any(p in mensaje for p in palabras)

    # ------------------------------------------------------------
    # BÚSQUEDA ESPECÍFICA EN BASES DE DATOS
    # ------------------------------------------------------------

    def _buscar_lugar_turistico(self, mensaje):
        """
        Detecta si se menciona un lugar turístico por nombre exacto o parcial.
        """
        coincidencia = self.repo.buscar_en_turismo(mensaje)
        return coincidencia is not None

    def _buscar_hotel(self, mensaje):
        coincidencia = self.repo.buscar_en_hoteles(mensaje)
        return coincidencia is not None

    def _buscar_restaurante(self, mensaje):
        coincidencia = self.repo.buscar_en_restaurantes(mensaje)
        return coincidencia is not None


