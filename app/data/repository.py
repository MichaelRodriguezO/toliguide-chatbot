# -*- coding: utf-8 -*-

"""
repository.py
--------------
Repositorio central de datos.
Clean Architecture — capa de datos.
"""

from app.data.info_data import (
    DATA,
    saludos,
    despedidas,
    agradecimientos,
    preguntas_frecuentes,
    fallback_responses,
    intenciones_clave,
    frases_prohibidas
)

from app.utils.normalizer import normalizar_texto as normalize_text


# Extraemos los diccionarios reales desde DATA
turismo = DATA.get("turismo", {})
hoteles = DATA.get("hoteles", {})
restaurantes = DATA.get("restaurantes", {})

# Si necesitas palabras comunes, defínelas aquí o en info_data
palabras_comunes = {"de", "la", "el", "en", "los", "las", "un", "una"}

# Activadores deben venir de info_data si quieres usarlos
activadores_intencion = intenciones_clave


class Repository:

    # ------------------------------------------------------------
    # SALUDOS / DESPEDIDAS / AGRADECIMIENTOS
    # ------------------------------------------------------------
    @staticmethod
    def get_saludos():
        return saludos

    @staticmethod
    def get_despedidas():
        return despedidas

    @staticmethod
    def get_agradecimientos():
        return agradecimientos

    # ------------------------------------------------------------
    # PREGUNTAS FRECUENTES
    # ------------------------------------------------------------
    @staticmethod
    def get_preguntas_frecuentes():
        return preguntas_frecuentes

    @staticmethod
    def get_respuesta_pregunta_clave(palabra_clave):
        return preguntas_frecuentes.get(palabra_clave)

    # ------------------------------------------------------------
    # TURISMO
    # ------------------------------------------------------------
    @staticmethod
    def get_turismo_categorias():
        return turismo

    @staticmethod
    def get_turismo_categoria(nombre_categoria):
        return turismo.get(nombre_categoria)

    @staticmethod
    def get_turismo_lugares():
        lugares = []
        for categoria in turismo.values():
            for lugar in categoria.keys():
                lugares.append(lugar)
        return lugares

    @staticmethod
    def get_info_lugar_turistico(nombre_lugar):
        nombre_normalizado = normalize_text(nombre_lugar)
        for categoria in turismo.values():
            for lugar, descripcion in categoria.items():
                if normalize_text(lugar) == nombre_normalizado:
                    return descripcion
        return None

    # ------------------------------------------------------------
    # HOTELES
    # ------------------------------------------------------------
    @staticmethod
    def get_hoteles():
        return hoteles

    @staticmethod
    def get_lista_hoteles():
        return list(hoteles.keys())

    @staticmethod
    def get_info_hotel(nombre_hotel):
        nombre_normalizado = normalize_text(nombre_hotel)
        for hotel, descripcion in hoteles.items():
            if normalize_text(hotel) == nombre_normalizado:
                return descripcion
        return None

    # ------------------------------------------------------------
    # RESTAURANTES
    # ------------------------------------------------------------
    @staticmethod
    def get_restaurantes():
        return restaurantes

    @staticmethod
    def get_lista_restaurantes():
        return list(restaurantes.keys())

    @staticmethod
    def get_info_restaurante(nombre_restaurante):
        nombre_normalizado = normalize_text(nombre_restaurante)
        for sitio, descripcion in restaurantes.items():
            if normalize_text(sitio) == nombre_normalizado:
                return descripcion
        return None

    # ------------------------------------------------------------
    # BÚSQUEDA INTELIGENTE
    # ------------------------------------------------------------
    @staticmethod
    def buscar_coincidencia(nombre, dataset):
        palabras_usuario = set(normalize_text(nombre).split()) - palabras_comunes

        for key in dataset:
            palabras_lugar = set(normalize_text(key).split()) - palabras_comunes
            if palabras_usuario & palabras_lugar:
                return key

        return None

    @staticmethod
    def buscar_en_turismo(nombre):
        for categoria in turismo.values():
            coincidencia = Repository.buscar_coincidencia(nombre, categoria)
            if coincidencia:
                return coincidencia
        return None

    @staticmethod
    def buscar_en_hoteles(nombre):
        return Repository.buscar_coincidencia(nombre, hoteles)

    @staticmethod
    def buscar_en_restaurantes(nombre):
        return Repository.buscar_coincidencia(nombre, restaurantes)

    # ------------------------------------------------------------
    # ACTIVADORES DE INTENCIÓN
    # ------------------------------------------------------------
    @staticmethod
    def get_activadores():
        return activadores_intencion

        @staticmethod
    def buscar_lugar(texto):
        """Busca coincidencias en lugares, hoteles y restaurantes."""
        texto = texto.lower()

        # Buscar en lugares turísticos
        lugar = Repository.buscar_en_lugares(texto)
        if lugar:
            return lugar["nombre"], lugar["descripcion"]

        # Buscar en hoteles
        hotel = Repository.buscar_en_hoteles(texto)
        if hotel:
            return hotel["nombre"], hotel["descripcion"]

        # Buscar en restaurantes
        restaurante = Repository.buscar_en_restaurantes(texto)
        if restaurante:
            return restaurante["nombre"], restaurante["descripcion"]

        return None, None

