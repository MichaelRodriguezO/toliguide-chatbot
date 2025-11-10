# -*- coding: utf-8 -*-

"""
sanitizer.py
----------------
Sanitiza el texto del usuario eliminando contenido potencialmente peligroso.
Protege contra:
  ✅ etiquetado HTML malicioso
  ✅ scripts
  ✅ comandos shell
  ✅ código no deseado
  ✅ exceso de espacios
"""

import re
import html


def sanitize_text(texto):
    """
    Sanitiza un mensaje eliminando HTML, JS y caracteres peligrosos.
    """

    if not isinstance(texto, str):
        return ""

    # 1. Convertir entidades HTML peligrosas
    texto = html.escape(texto)

    # 2. Eliminar tags HTML <script> y similares
    texto = re.sub(r"<\s*script[^>]*>.*?<\s*/\s*script\s*>", "", texto, flags=re.IGNORECASE | re.DOTALL)

    # 3. Eliminar cualquier etiqueta HTML por seguridad
    texto = re.sub(r"<[^>]+>", "", texto)

    # 4. Eliminar comandos tipo JS o shell
    texto = re.sub(r"(javascript:|onclick=|onload=|cmd.exe|powershell|bash -i|wget\s+)", "", texto, flags=re.IGNORECASE)

    # 5. Eliminar secuencias tipo SQL injection
    texto = re.sub(r"(drop table|select \*|delete from|insert into|update set)", "", texto, flags=re.IGNORECASE)

    # 6. Eliminar caracteres repetidos
    texto = limpiar_caracteres_repetidos(texto)

    # 7. Limpiar doble espacio
    texto = re.sub(r"\s+", " ", texto).strip()

    return texto


def limpiar_caracteres_repetidos(texto):
    """
    Reduce caracteres repetidos: "holaaaaaa" -> "hola"
    No afecta a caracteres normales.
    """

    # Reemplaza secuencias largas del mismo carácter
    return re.sub(r"(.)\1{2,}", r"\1", texto)
