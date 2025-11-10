## -*- coding: utf-8 -*-

"""
session_manager.py
-------------------
Administra sesiones y contexto de conversación.
Se encarga de almacenar el historial del usuario y la última intención detectada.
"""

class SessionManager:

    def __init__(self):
        # Diccionario maestro
        # Estructura:
        # sesiones = {
        #    "id_sesion": {
        #         "historial": [],
        #         "ultima_intencion": None
        #    }
        # }
        self.sesiones = {}


    # ------------------------------------------------------------
    # CREAR / INICIAR SESIÓN
    # ------------------------------------------------------------
    def crear_sesion(self, session_id):
        """Si la sesión no existe, la crea."""
        if session_id not in self.sesiones:
            self.sesiones[session_id] = {
                "historial": [],
                "ultima_intencion": None
            }


    # ------------------------------------------------------------
    # OBTENER CONTEXTO
    # ------------------------------------------------------------
    def obtener_contexto(self, session_id):
        """
        Devuelve el contexto completo de la sesión:
        historial + última intención
        """
        if session_id not in self.sesiones:
            self.crear_sesion(session_id)

        return self.sesiones[session_id]


    # ------------------------------------------------------------
    # ACTUALIZAR CONTEXTO
    # ------------------------------------------------------------
    def actualizar_contexto(self, session_id, nuevo_mensaje, nueva_intencion=None):
        """
        Guarda el mensaje en el historial y opcionalmente actualiza la intención.
        """
        if session_id not in self.sesiones:
            self.crear_sesion(session_id)

        self.sesiones[session_id]["historial"].append(nuevo_mensaje)

        if nueva_intencion:
            self.sesiones[session_id]["ultima_intencion"] = nueva_intencion


    # ------------------------------------------------------------
    # REINICIAR SESIÓN / BORRAR CONTEXTO
    # ------------------------------------------------------------
    def reiniciar_sesion(self, session_id):
        """Elimina el historial e intención de la sesión."""
        self.sesiones[session_id] = {
            "historial": [],
            "ultima_intencion": None
        }

        return list(self.sessions.keys())

    def session_exists(self, session_id):
        return session_id in self.sessions
