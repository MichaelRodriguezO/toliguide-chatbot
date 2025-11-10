# -*- coding: utf-8 -*-

"""
info_data.py
------------------
Repositorio de datos estáticos para el chatbot turístico.
Incluye turismo, hoteles, restaurantes, saludos, despedidas y fallback.
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
            "Jardín Botánico San Jorge": "Una reserva natural urbana con senderos ecológicos."
        },
        "cultura": {
            "Teatro Tolima": "Escenario cultural de conciertos y obras.",
            "Conservatorio del Tolima": "Símbolo nacional de formación musical.",
            "Museo de Arte del Tolima": "Cuenta con exposiciones permanentes y temporales."
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
        "Punta del Este": "Restaurante tradicional de mariscos.",
        "El Fogón Llanero": "Comida típica llanera, famosa por la mamona.",
        "La Parrilla de Marcos": "Carnes a la parrilla de excelente calidad."
    }
}

# ===============================================================
# SALUDOS
# ===============================================================

saludos = [
    "¡Hola! ¿Cómo puedo ayudarte hoy?",
    "¡Bienvenido! ¿En qué puedo colaborar?",
    "¡Hola! ¿Buscas información turística?"
]

# ===============================================================
# DESPEDIDAS
# ===============================================================

despedidas = [
    "¡Hasta pronto! 😊",
    "¡Gracias por usar Toliguide! 🌄",
    "¡Que tengas un excelente día!",
    "¡Vuelve cuando quieras para más información!"
]

# ===============================================================
# RESPUESTAS SI NO SE ENTIENDE
# ===============================================================

fallback_responses = [
    "Lo siento, no entendí tu mensaje. ¿Podrías reformularlo?",
    "No tengo información sobre eso, ¿te gustaría que te recomiende lugares turísticos?",
    "Puedo ayudarte con turismo, hoteles o restaurantes de Ibagué. ¿Qué deseas saber?"
]

# ===============================================================
# FRASES PROHIBIDAS O SENSIBLES
# ===============================================================

frases_prohibidas = [
    "bomba",
    "amenaza",
    "armas",
    "atentado",
    "matar",
    "terrorismo"
]

# ===============================================================
# INTENCIONES (si tu clasificador los usa)
# ===============================================================

intenciones_clave = {
    "saludo": ["hola", "buenas", "saludos", "hey", "qué tal"],
    "despedida": ["adios", "hasta luego", "nos vemos", "chao"],
    "turismo": ["lugar", "sitio", "turismo", "visitar"],
    "hotel": ["hotel", "hospedaje", "alojamiento"],
    "restaurante": ["comida", "restaurante", "cena", "almuerzo"]
}
