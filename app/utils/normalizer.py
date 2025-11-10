# -*- coding: utf-8 -*-

"""
normalizer.py
----------------
Se encarga de normalizar el texto de entrada para facilitar la detección
de intenciones. Limpia tildes, caracteres especiales y uniformiza el texto.
"""

import unicodedata
import re


def normalizar_texto(texto):
    """
    Normaliza el texto eliminando:
      ✅ mayúsculas
      ✅ tildes (á→a, é→e...)
      ✅ emojis
      ✅ puntuación
      ✅ caracteres unicode raros
      ✅ espacios múltiples
    """

    if not isinstance(texto, str):
        return ""

    # 1. Convertir a minúsculas
    texto = texto.lower().strip()

    # 2. Eliminar emojis
    texto = remove_emojis(texto)

    # 3. Normalizar tildes
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")

    # 4. Quitar caracteres no alfanuméricos
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)

    # 5. Comprimir espacios
    texto = re.sub(r"\s+", " ", texto).strip()

    return texto


def remove_emojis(text):
    """
    Elimina emojis y caracteres especiales no útiles
    """
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticones
        u"\U0001F300-\U0001F5FF"  # símbolos
        u"\U0001F680-\U0001F6FF"  # transporte
        u"\U0001F1E0-\U0001F1FF"  # banderas
        u"\U00002500-\U00002BEF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r"", text)
