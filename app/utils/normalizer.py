# -*- coding: utf-8 -*-

"""
normalizer.py
----------------
Se encarga de normalizar el texto de entrada para facilitar la detección
de intenciones. Limpia tildes, caracteres especiales y uniformiza el texto.

Este módulo asegura que cualquier cadena de texto ingresada sea transformada
a una forma estable, comparable y segura para procesamiento lógico.
"""

import unicodedata
import re


def normalize_text(texto):
    """
    Normaliza el texto eliminando:
      ✅ mayúsculas
      ✅ tildes (á→a, é→e...)
      ✅ caracteres unicode raros
      ✅ emojis
      ✅ puntuación
      ✅ espacios múltiples

    Retorna una versión limpia del mensaje del usuario.
    """

    if not isinstance(texto, str):
        return ""

    # 1. Convertir a minúsculas
    texto = texto.lower().strip()

    # 2. Eliminar emojis y caracteres no alfabéticos (mantiene espacios)
    #    Esto elimina símbolos que no afectan comprensión textual.
    texto = remove_emojis(texto)

    # 3. Normalizar tildes con unicodedata
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")

    # 4. Eliminar caracteres que no sean letras, números o espacios
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)

    # 5. Reducir espacios múltiples
    texto = re.sub(r"\s+", " ", texto).strip()

    return texto


def remove_emojis(text):
    """
    Elimina emojis y caracteres especiales que no son útiles
    en el procesamiento semántico del mensaje.
    """
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Símbolos y pictogramas
        u"\U0001F680-\U0001F6FF"  # Transporte y mapas
        u"\U0001F1E0-\U0001F1FF"  # Banderas
        u"\U00002500-\U00002BEF"  # Chino / radicales
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )

    return emoji_pattern.sub(r"", text)
