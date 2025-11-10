# -*- coding: utf-8 -*-

"""
validator.py
----------------
Valida el texto del usuario antes de ser procesado por el bot.

El objetivo es evitar que el sistema procese:
  ✅ mensajes vacíos
  ✅ spam
  ✅ texto ilegible
  ✅ solo emojis
  ✅ solo números
  ✅ mensajes demasiado largos
"""

import re


def is_valid_message(texto):
    """
    Retorna True si el mensaje del usuario es válido para procesar.
    Caso contrario retorna False.
    """

    if not isinstance(texto, str):
        return False

    texto = texto.strip()

    # 1) Mensaje vacío
    if texto == "" or texto is None:
        return False

    # 2) Limitar longitud máxima para evitar abusos
    if len(texto) > 500:
        return False

    # 3) Detectar mensajes con solo emojis
    if es_solo_emojis(texto):
        return False

    # 4) Detectar mensajes con solo números
    if texto.isnumeric():
        return False

    # 5) Detectar mensajes con ruido extremadamente repetitivo
    if es_ruido_repetitivo(texto):
        return False

    # 6) Evitar cadenas sin letras ni palabras reales
    if not contiene_palabras(texto):
        return False

    return True


def es_solo_emojis(texto):
    """
    Detecta si el texto contiene solo emojis o símbolos Unicode sin palabras.
    """

    patron = r"^[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\s]+$"
    return re.match(patron, texto) is not None


def es_ruido_repetitivo(texto):
    """
    Detecta cadenas de un solo caracter repetido ["aaaaaa", "jjjjjj"]
    o patrones repetitivos que no significan nada.
    """

    # cualquier caracter repetido más de 6 veces
    if re.match(r"^(.)\1{6,}$", texto):
        return True

    # secuencias tipo "asdkljasdkjlk" sin vocales o estructura
    if len(re.findall(r"[aeiouáéíóú]", texto, re.IGNORECASE)) == 0 and len(texto) > 12:
        return True

    return False


def contiene_palabras(texto):
    """
    Verifica que haya al menos una palabra reconocible.
    """

    # Debe contener letras
    contiene_letras = bool(re.search(r"[a-zA-ZáéíóúñÁÉÍÓÚÑ]", texto))
    if not contiene_letras:
        return False

    # No ser solo símbolos especiales
    if re.match(r"^[^a-zA-ZáéíóúñÁÉÍÓÚÑ0-9]+$", texto):
        return False

    return True
