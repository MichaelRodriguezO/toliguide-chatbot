# -*- coding: utf-8 -*-

"""
info_data.py
-------------
Contiene todas las bases de datos estáticas del asistente ToliGuide.
Incluye: saludos, despedidas, preguntas frecuentes, categorías turísticas,
hoteles, restaurantes y palabras de activación para intenciones.
"""

saludos = [
    "hola", "holaaa", "holi", "hello", "hey", "buenas",
    "wenas", "qué más", "que mas", "ola", "saludos", "qué onda",
    "buen día", "buenas tardes", "buenas noches", "empezar", "inicio"
]

despedidas = [
    "adios", "bye", "hasta luego", "nos vemos", "hasta pronto",
    "gracias", "muchas gracias", "salir", "cerrar", "chau", "chao"
]

agradecimientos = [
    "gracias", "muchas gracias", "te agradezco", " mil gracias", "super", "excelente"
]

preguntas_frecuentes = {
    "horario": "Los horarios pueden variar según el lugar. ¿Deseas saber el horario de un sitio en particular?",
    "precio": "Los precios son aproximados y pueden cambiar. Indica un sitio específico para darte información más precisa.",
    "temperatura": "El clima en Ibagué suele ser cálido con temperaturas entre 23°C y 28°C.",
    "como llegar": "Puedo ayudarte con la ubicación si me dices el sitio exacto.",
    "transporte": "En Ibagué encuentras taxis, busetas y transporte por apps como InDriver y Didi."
}

# ------------------------------------------------------------
# Categorías de información turística organizada por temas
# ------------------------------------------------------------
turismo = {
    "historia": {
        "plaza de bolívar y catedral primada": "Corazón histórico de Ibagué con arquitectura colonial y campanas francesas.",
        "parque manuel murillo toro": "Plaza central con importancia política y cultural en el Tolima.",
        "museo panóptico": "Antigua prisión en forma de cruz griega, ahora transformada en museo moderno.",
        "barrios la pola y belén": "Casonas antiguas y arquitectura colonial.",
        "teatro tolima": "Construcción de 1911, considerado ícono cultural."
    },

    "naturaleza": {
        "jardín botánico san jorge": "Senderos ecológicos, miradores y naturaleza pura.",
        "cañón del combeima": "Paisajes, termales y acceso a rutas hacia el Nevado del Tolima.",
        "parque museo la martinica": "Miradores, cascadas y rutas de aventura.",
        "santa fe de los guaduales": "Reserva ecológica con senderos y alojamiento.",
        "fundación orquídeas del tolima": "Más de 160 especies de orquídeas nativas."
    },

    "cultura": {
        "museo de arte del tolima": "Arte colombiano, exposiciones temporales y colección permanente.",
        "museo antropologico ut": "Enfoque en las culturas indígenas de la región.",
        "parque centenario": "Centro de eventos y festivales.",
        "conservatorio del tolima": "Fundado en 1906, cuna de músicos reconocidos.",
        "parque de la música": "Espacio para conciertos y expresiones artísticas."
    }
}

# ------------------------------------------------------------
# Información de hoteles recomendados
# ------------------------------------------------------------
hoteles = {
    "sonesta hotel ibagué": "Hotel 5★ con piscina, sauna, restaurante y excelente reputación.",
    "hotel estelar altamira": "Hotel 4★ con spa, piscina y restaurante. Ubicación premium.",
    "casa morales": "Hotel familiar con piscina cubierta y espacios amplios.",
    "hotel dann combeima": "Hotel céntrico, ideal para familias o trabajo.",
    "eco star hotel": "Moderno, económico (~$170.000 COP) y excelente ubicación."
}

# ------------------------------------------------------------
# Información de restaurantes
# ------------------------------------------------------------
restaurantes = {
    "sonora parrilla bar": "Carnes a la parrilla y ambiente moderno.",
    "sr. miyagi asian cuisine": "Fusión japonesa, tailandesa y china.",
    "punta del este restaurante bar": "Mariscos, parrilla y vista espectacular.",
    "la parrilla de marcos": "Especialidad en carnes a la brasa.",
    "chorilongo": "Choripanes y comida callejera gourmet.",
    "la ricotta": "Cocina italiana con ambiente romántico.",
    "el fogón llanero": "Mamona y carne a la llanera.",
    "restaurante altavista": "Vista panorámica y comida internacional.",
    "maria y el mar": "Mariscos de alta calidad.",
    "la casona comida típica": "Tamal, lechona y platos típicos."
}

# ------------------------------------------------------------
# Palabras comunes para filtrar coincidencias
# ------------------------------------------------------------
palabras_comunes = {
    "de", "la", "el", "y", "en", "a", "del", "con", "una", "un",
    "por", "para", "donde", "que", "cual", "como", "cuales", "las", "los"
}

# ------------------------------------------------------------
# Activadores de intención agrupados
# ------------------------------------------------------------
activadores_intencion = {
    "saludo": saludos,
    "despedida": despedidas,
    "agradecimiento": agradecimientos,
    "turismo": ["turismo", "sitios", "lugares", "turisticos", "tours", "paseo"],
    "hoteles": ["hotel", "hospedaje", "alojamiento", "dormir"],
    "restaurantes": ["restaurante", "comida", "comer", "cena", "almuerzo"],
    "preguntas": list(preguntas_frecuentes.keys()),
}
