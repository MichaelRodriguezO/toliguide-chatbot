from flask import Flask, request, jsonify, render_template
import os
import difflib

app = Flask(__name__)

saludos = ["hola", "wenas", "buenas", "qué más", "holi", "saludos", "empezar", "inicio", "toli", "hey"]

stopwords = {"de", "la", "el", "y", "en", "a", "del", "con", "una", "un", "por", "para"}

# Mapeo de intenciones por sinónimos
intenciones = {
    "comida típica": ["comida rica", "plato típico", "tamal", "lechona"],
    "romántico": ["romántico", "pareja", "plan en pareja", "lugar para dos"],
    "económico": ["barato", "económico", "accesible", "mochilero"],
    "vista": ["mirador", "vista bonita", "panorámica", "con vista"],
    "mariscos": ["mariscos", "pescado", "comida de mar"]
}

# Respuestas fijas por frases frecuentes
faq_respuestas = {
    "qué hacer en ibagué": "Te recomiendo visitar el Cañón del Combeima, el Panóptico y el Parque La Martinica.",
    "dónde ir con niños": "Puedes visitar el Jardín Botánico San Jorge, el Parque de la Música y el Parque Museo La Martinica.",
    "dónde comer barato": "Algunas opciones económicas son Chorilongo, Eco Star y Bahareque Hostal.",
    "comida típica": "Prueba La Casona Comida Típica, El Fogón Llanero o La Parrilla de Marcos."
}

# Base de datos resumida (ver versión completa en tu proyecto)
info = {
    "turismo": {
        "historia": {
            "teatro tolima": "Joya arquitectónica de 1911 con programación cultural.",
            "plaza de bolívar y catedral primada": "Centro histórico y religioso de Ibagué."
        },
        "naturaleza": {
            "cañón del combeima": "Ruta natural con termales y vistas al Nevado.",
            "jardín botánico san jorge": "Bosque con senderos, miradores y biodiversidad."
        },
        "cultura": {
            "parque de la música": "Escenario musical con murales y eventos.",
            "conservatorio del tolima": "Semillero de músicos y patrimonio de la ciudad."
        }
    },
    "hoteles": {
        "sonesta hotel ibagué": "Hotel 5★ con piscina, restaurante y buena reputación.",
        "eco star hotel": "Hotel económico (~$170.000 COP), moderno y bien ubicado."
    },
    "restaurantes": {
        "la parrilla de marcos": "Carnes y comida típica, muy tradicional.",
        "maria y el mar": "Mariscos y cocina costeña, sofisticado.",
        "la ricotta": "Restaurante italiano, ideal para parejas.",
        "chorilongo": "Comida callejera gourmet, opción juvenil."
    }
}

def link_maps(nombre):
    return f"📍 Ver en Google Maps: https://www.google.com/maps/search/{'+'.join(nombre.split())}"

# Buscar por similitud usando difflib
def buscar_similar(user_input, opciones):
    coincidencias = difflib.get_close_matches(user_input, opciones, n=1, cutoff=0.7)
    return coincidencias[0] if coincidencias else None

# Intenciones por sinónimos
def detectar_intencion(user_input):
    for intento, expresiones in intenciones.items():
        for palabra in expresiones:
            if palabra in user_input:
                return intento
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = "No entendí tu mensaje. Escribe: turismo, hoteles o restaurantes."

    if any(s in user_input for s in saludos):
        return jsonify({"response": "¡Hola! Soy ToliGuide, tu guía turístico de Ibagué 🇨🇴. ¿Qué deseas conocer hoy?"})

    # FAQ exactas
    for frase, rpta in faq_respuestas.items():
        if frase in user_input:
            return jsonify({"response": rpta})

    # Intención detectada por sinónimo
    intento = detectar_intencion(user_input)
    if intento == "comida típica":
        return jsonify({"response": faq_respuestas["comida típica"]})
    elif intento == "romántico":
        return jsonify({"response": "💑 Lugares románticos: La Ricotta, Restaurante Altavista, Hotel Dann Combeima."})
    elif intento == "económico":
        return jsonify({"response": "💸 Opciones económicas: Chorilongo, Eco Star Hotel, Bahareque Hostal."})
    elif intento == "vista":
        return jsonify({"response": "🌇 Lugares con buena vista: Restaurante Altavista, La Martinica, Cañón del Combeima."})
    elif intento == "mariscos":
        return jsonify({"response": "🦐 Restaurantes con mariscos: Maria y el Mar, Punta del Este."})

    # Mostrar categorías
    if "turismo" in user_input:
        out = "🏞 Lugares turísticos:\n"
        for cat, sitios in info["turismo"].items():
            emoji = {"historia": "📜", "naturaleza": "🌿", "cultura": "🎭"}.get(cat, "•")
            out += f"\n{emoji} {cat.capitalize()}:\n• " + "\n• ".join(sitios.keys())
        return jsonify({"response": out})

    elif "hotel" in user_input:
        return jsonify({"response": "🛌 Hoteles recomendados:\n• " + "\n• ".join(info["hoteles"].keys())})

    elif "restaurante" in user_input or "comida" in user_input:
        return jsonify({"response": "🍽 Restaurantes destacados:\n• " + "\n• ".join(info["restaurantes"].keys())})

    # Buscar coincidencia directa o similar
    todas_opciones = []
    descripciones = {}

    for categoria in info:
        if categoria == "turismo":
            for subcat in info[categoria].values():
                for lugar, desc in subcat.items():
                    todas_opciones.append(lugar)
                    descripciones[lugar] = desc
        else:
            for lugar, desc in info[categoria].items():
                todas_opciones.append(lugar)
                descripciones[lugar] = desc

    mejor_coincidencia = buscar_similar(user_input, todas_opciones)
    if mejor_coincidencia:
        desc = descripciones[mejor_coincidencia]
        return jsonify({"response": f"{mejor_coincidencia.title()}:\n{desc}\n{link_maps(mejor_coincidencia)}"})

    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
