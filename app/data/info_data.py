# -*- coding: utf-8 -*-

"""
info_data.py
------------------
Repositorio de datos estáticos del chatbot turístico.
Incluye saludos, despedidas, preguntas frecuentes, categorías,
lugares, hoteles, restaurantes y frases de fallback.
"""

# ===============================================================
# LISTAS DE RESPUESTAS BÁSICAS
# ===============================================================

saludos = [
    "¡Hola! ¿Cómo puedo ayudarte hoy?",
    "¡Bienvenido a ToliGuide! 😊",
    "¡Hola! ¿Buscas información turística o recomendaciones?",
    "¡Qué gusto verte por aquí! ¿En qué te puedo ayudar?"
]

despedidas = [
    "¡Hasta luego! 😊",
    "¡Gracias por usar ToliGuide! 🌄",
    "¡Cuídate y vuelve pronto!",
    "¡Que tengas un excelente día!"
]

agradecimientos = [
    "¡Con gusto! 😊",
    "¡Siempre feliz de ayudar!",
    "¡Gracias a ti por preguntar!",
    "¿Necesitas algo más?"
]

fallback_responses = [
    "No estoy seguro de entender, ¿puedes explicarlo de otra forma?",
    "Puedo ayudarte con turismo, hoteles o restaurantes de Ibagué.",
    "No tengo esa información aún, pero puedo sugerirte lugares.",
    "Reformula tu pregunta para darte una mejor respuesta."
]

frases_prohibidas = [
    "bomba", "arma", "matar", "atentado", "amenaza", "terrorismo",
    "narco", "secuestro", "explosivo"
]

# ===============================================================
# PREGUNTAS FRECUENTES (VARIABLE QUE FALTABA)
# ===============================================================

preguntas_frecuentes = {
    "horarios": "Muchos sitios turísticos abren desde las 8am hasta las 6pm.",
    "clima": "El clima en Ibagué suele ser templado, entre 21°C y 28°C.",
    "transporte": "Puedes moverte en busetas, taxis y apps como InDriver.",
    "seguridad": "Las zonas turísticas principales son seguras, pero siempre mantén precaución."
}

# ===============================================================
# INFORMACIÓN PRINCIPAL DE CONTENIDO
# ===============================================================

DATA = {
    "turismo": {
        "historia": {
            "Catedral Primada de Ibagué": "Templo emblemático en el centro histórico.",
            "Plaza de Bolívar": "Icono cultural y político de la ciudad."
        },
        "naturaleza": {
            "Cañón del Combeima": "Corriente natural con senderismo y miradores.",
            "Nevado del Tolima": "Imponente cumbre del Parque Los Nevados.",
            "Jardín Botánico San Jorge": "Reserva natural con senderos ecológicos."
        },
        "cultura": {
            "Teatro Tolima": "Lugar histórico de eventos y presentaciones.",
            "Conservatorio del Tolima": "Famoso centro musical.",
            "Museo de Arte del Tolima": "Exposición de arte moderno y clásico."
        }
    },

    "hoteles": {
        "Hotel Dann Combeima": "Hotel elegante ubicado en el centro.",
        "Hotel Estelar Altamira": "Hotel 5 estrellas con jardines y piscina.",
        "Eco Star Hotel": "Hospedaje moderno y económico.",
        "Casa Morales": "Hotel familiar con piscina y zonas de recreo."
    },

    "restaurantes": {
        "María y el Mar": "Especialidad en mariscos frescos.",
        "La Ricotta": "Excelente comida italiana y ambiente tranquilo.",
        "Punta del Este": "Mariscos con preparación tradicional.",
        "El Fogón Llanero": "Comida típica llanera, famosa por su carne a la llanera.",
        "La Parrilla de Marcos": "Carnes a la parrilla de primera calidad."
    }
}

# ===============================================================
# INTENCIONES PARA EL CLASIFICADOR
# ===============================================================

intenciones_clave = {
    "saludo": ["hola", "buenas", "saludos", "hey", "holi"],
    "despedida": ["chao", "adios", "hasta luego", "nos vemos"],
    "agradecimiento": ["gracias", "muy amable", "te agradezco"],
    "turismo": ["turismo", "lugares", "visitar", "planes", "sitio"],
    "hotel": ["hotel", "hospedaje", "alojamiento"],
    "restaurante": ["restaurante", "comida", "cenar", "almorzar"],
    "pregunta_frecuente": ["horarios", "clima", "seguridad", "transporte"]
}

