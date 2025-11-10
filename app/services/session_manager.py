# -*- coding: utf-8 -*-

"""
session_manager.py
-------------------
Maneja las sesiones de chat para cada usuario.
Permite almacenar el historial de mensajes del usuario y del bot,
obtener el último mensaje, limpiar sesiones y mantener contexto básico.

Clean Architecture -> Capa de servicios
"""

import time


class SessionManager:

    def __init__(self):
        # Diccionario en memoria: { session_id: { "user": [], "bot": [] } }
        self.sessions = {}

        # Máximo de mensajes a mantener en memoria por sesión
        self.max_historial = 20

        # Auto-limpieza de sesiones antiguas (tiempo en segundos)
        self.tiempo_expiracion = 3600  # 1 hora de inactividad

        # Registro de timestamps por sesión
        self.session_timestamps = {}

    # ------------------------------------------------------------
    # CREACIÓN Y MANTENIMIENTO DE SESIONES
    # ------------------------------------------------------------

    def _ensure_session(self, session_id):
        """
        Crea la sesión si no existe e inicializa estructura de datos.
        """
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "user": [],
                "bot": []
            }

        # Actualiza timestamp
        self.session_timestamps[session_id] = time.time()

    def _limpiar_sesion_si_expirada(self, session_id):
        """
        Elimina sesiones inactivas para liberar memoria.
        """
        timestamp = self.session_timestamps.get(session_id, time.time())
        if time.time() - timestamp > self.tiempo_expiracion:
            self.limpiar_sesion(session_id)

    # ------------------------------------------------------------
    # MÉTODOS DE GUARDAR MENSAJES
    # ------------------------------------------------------------

    def save_user_message(self, session_id, message):
        """
        Guarda un mensaje del usuario.
        """
        self._limpiar_sesion_si_expirada(session_id)
        self._ensure_session(session_id)

        self.sessions[session_id]["user"].append(message)
        self._reducir_historial(session_id)

    def save_bot_message(self, session_id, message):
        """
        Guarda respuesta del bot.
        """
        self._limpiar_sesion_si_expirada(session_id)
        self._ensure_session(session_id)

        self.sessions[session_id]["bot"].append(message)
        self._reducir_historial(session_id)

    # ------------------------------------------------------------
    # OBTENER INFORMACIÓN DE LA SESIÓN
    # ------------------------------------------------------------

    def get_last_user_message(self, session_id):
        """
        Obtiene el último mensaje del usuario.
        """
        if session_id not in self.sessions:
            return None

        historial = self.sessions[session_id]["user"]
        return historial[-1] if historial else None

    def get_last_bot_message(self, session_id):
        """
        Obtiene el último mensaje del bot.
        """
        if session_id not in self.sessions:
            return None

        historial = self.sessions[session_id]["bot"]
        return historial[-1] if historial else None

    def get_historial(self, session_id):
        """
        Devuelve un diccionario con el historial completo de la sesión.
        """
        return self.sessions.get(session_id, {"user": [], "bot": []})

    # ------------------------------------------------------------
    # LIMPIEZA DE HISTORIAL
    # ------------------------------------------------------------

    def limpiar_sesion(self, session_id):
        """
        Elimina toda la información relacionada a la sesión.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
        if session_id in self.session_timestamps:
            del self.session_timestamps[session_id]

    def limpiar_todas_las_sesiones(self):
        """
        Limpia todas las sesiones activas.
        """
        self.sessions = {}
        self.session_timestamps = {}

    def _reducir_historial(self, session_id):
        """
        Mantiene solo los últimos N mensajes para ahorro de memoria.
        """
        if session_id not in self.sessions:
            return

        for tipo in ["user", "bot"]:
            if len(self.sessions[session_id][tipo]) > self.max_historial:
                self.sessions[session_id][tipo] = self.sessions[session_id][tipo][-self.max_historial:]

    # ------------------------------------------------------------
    # UTILIDADES ADICIONALES
    # ------------------------------------------------------------

    def get_session_ids(self):
        """
        Devuelve todas las sesiones activas.
        """
        return list(self.sessions.keys())

    def session_exists(self, session_id):
        return session_id in self.sessions
