# -*- coding: utf-8 -*-

"""
info_data.py
------------------
Repositorio de datos estáticos para el chatbot turístico.
Incluye turismo, hoteles, restaurantes, saludos, despedidas,
agradecimientos, fallbacks, frases prohibidas e intenciones.
"""

# ===============================================================
# DATOS PRINCIPALES DEL CHATBOT
# ===============================================================

DATA = {
    "turismo": {
        "historia": {
            "Catedral Primada de Ibagué": "Templo emblemático ubicado en el centro histórico.",
            "Plaza de Bolívar": "Punto histórico principal de Ibagué, rodeado de arquitectura colonial."
        },
        "naturaleza": {
            "Cañón del Combeima": "El destino ecológico más representativo de Ibagué.",
            "Nevado del Tolima": "Montaña icónica del parque Los Nevados.",
            "Jardín Botánico San Jorge": "Reserva natural urbana con senderos verdes."
        },
        "cultura": {
            "Teatro Tolima": "Escenario cultural de conciertos y obras.",
            "Conservatorio del Tolima": "Centro emblemático de formación musical.",
            "Museo de Arte del Tolima": "Exposiciones permanentes y temporales."
        }
    },

    "hoteles": {
        "Hotel Dann Combeima": "Hotel céntrico de alta categoría.",
        "Hotel Estelar Altamira": "Hotel de lujo rodeado de áreas verdes.",
        "Eco Star Hotel": "Hospedaje económico moderno.",
        "Casa Morales": "Hotel familiar con piscina y spa."
    },

    "restaurantes": {
        "María y el Mar": "Especialidad en mariscos y pescados frescos.",
        "La Ricotta": "Comida italiana en ambiente romántico.",
        "Punta del Este": "Mariscos tradicionales.",
        "El Fogón Llanero": "Comida típica llanera, famosa por la mamona.",
        "La Parrilla de Marcos": "Carnes a la parrilla."
    }
}

# ===============================================================
# SALUDOS
# ===============================================================

saludos = [
    "¡Hola! ¿Cómo puedo ayudarte hoy?",
    "¡Bienvenido! ¿En qué puedo colaborar?",
    "¡Hola! ¿Buscas información turística?",
    "¡Bienvenido a ToliGuide! 😊"
]

# ===============================================================
# DESPEDIDAS
# ===============================================================

despedidas = [
    "¡Hasta pronto! 😊",
    "¡Gracias por usar ToliGuide! 🌄",
    "¡Que tengas un excelente día!",
    "¡Vuelve cuando quieras para más información!"
]

# ===============================================================
# AGRADECIMIENTOS (VARIABLE QUE TE FALTABA)
# ===============================================================

agradecimientos = [
    "¡Con gusto! 😊",
    "¡Para eso estoy! 🙌",
    "¡Me alegra ayudarte! 🌟",
    "¡Gracias a ti! ¿Necesitas algo más?"
]

# ===============================================================
# RESPUESTAS SI NO SE ENTIENDE
# ===============================================================

fallback_responses = [
    "No entendí muy bien, ¿podrías reformular tu pregunta?",
    "No tengo esa información. ¿Quieres que te recomiende lugares turísticos?",
    "Puedo ayudarte con turismo, hoteles o restaurantes de Ibagué. ¿Qué deseas saber?"
]

# ===============================================================
# FRASES PROHIBIDAS O CONTENIDO SENSIBLE
# ===============================================================

frases_prohibidas = [
    "bomba", "amenaza", "armas", "atentado", "matar", "terrorismo"
]

# ===============================================================
# INTENCIONES PARA CLASIFICADOR
# ===============================================================

intenciones_clave = {
    "saludo": ["hola", "buenas", "saludos", "hey", "qué tal"],
    "despedida": ["adios", "hasta luego", "nos vemos", "chao"],
    "agradecimiento": ["gracias", "te agradezco", "muy amable"],
    "turismo": ["turismo", "visitar", "lugar", "sitio"],
    "hotel": ["hotel", "hospedaje", "alojamiento"],
    "restaurante": ["comida", "restaurante", "cena", "almuerzo"]
}
