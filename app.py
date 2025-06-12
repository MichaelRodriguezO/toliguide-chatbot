from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Información detallada
info = {
    "introduccion": (
        "¡Hola! Soy ToliGuide, tu asistente turístico de Ibagué. "
        "Puedo ayudarte a conocer los lugares más importantes de la ciudad. "
        "Escribe 'turismo', 'hoteles' o 'restaurantes' para comenzar."
    ),
    "turismo": {
        "Catedral Primada": "Frente a la Plaza de Bolívar. Tiene un reloj suizo de 1929 y campanas francesas.",
        "Panóptico": "Antigua cárcel en forma de cruz, ahora museo y centro cultural.",
        "Museo de Arte del Tolima": "Obras de arte colombiano desde lo precolombino hasta contemporáneo.",
        "Jardín Botánico San Jorge": "60 hectáreas de bosque, miradores y senderos para ecoturismo.",
        "Cañón del Combeima": "Ruta natural con miradores, restaurantes, termales y senderismo al Nevado."
    },
    "hoteles": {
        "Sonesta Hotel Ibagué": "Hotel 5★ con piscina, sauna, restaurante y gimnasio. Muy buena calificación.",
        "Hotel Estelar Altamira": "Hotel 4★ con piscina, spa, restaurante y servicio a empresas.",
        "Casa Morales": "Hotel 3½★ ideal para convenciones, con piscina cubierta y restaurante.",
        "Dann Combeima": "Hotel 4★ popular entre familias, con buena ubicación y piscina.",
        "Eco Star Hotel": "Hotel económico y moderno con buena ubicación y calificación media."
    },
    "restaurantes": {
        "La Parrilla de Marcos": "Especialidad en carnes a la parrilla. Ambiente familiar.",
        "Rancho Mazorca": "Comida típica tolimense y ambiente rústico.",
        "Cuzco": "Restaurante de fusión peruana-colombiana con ambiente elegante.",
        "Palo Santo": "Comida gourmet colombiana con toques modernos."
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = "Lo siento, no entendí tu pregunta. Puedes escribir 'turismo', 'hoteles' o 'restaurantes'."

    if any(palabra in user_input for palabra in ["hola", "buenos días", "inicio", "empezar", "toli", "guía"]):
        response = info["introduccion"]

    elif "turismo" in user_input:
        lista = "\n".join(f"- {lugar}" for lugar in info["turismo"])
        response = "Aquí tienes algunos sitios turísticos en Ibagué:\n" + lista

    elif "hotel" in user_input:
        lista = "\n".join(f"- {hotel}" for hotel in info["hoteles"])
        response = "Estos son algunos hoteles en Ibagué:\n" + lista

    elif "restaurante" in user_input or "comer" in user_input:
        lista = "\n".join(f"- {restaurante}" for restaurante in info["restaurantes"])
        response = "Aquí tienes algunos restaurantes recomendados:\n" + lista

    # Buscar descripción específica de lugar/hotel/restaurante
    else:
        for categoria in ["turismo", "hoteles", "restaurantes"]:
            for nombre, descripcion in info[categoria].items():
                if nombre.lower() in user_input:
                    response = f"{nombre}: {descripcion}"

    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
