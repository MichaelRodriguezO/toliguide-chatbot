from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Base de datos simple (se puede mover a JSON o CSV luego)
data = {
    "turismo": [
        "Plaza de Bolívar y Catedral Primada",
        "Parque Centenario y Concha Acústica Garzón y Collazos",
        "Parque Manuel Murillo Toro",
        "Plazoleta Darío Echandía",
        "Museo de Arte del Tolima (MAT)",
        "Museo Panóptico",
        "Museo Antropológico de la Universidad del Tolima",
        "Conservatorio del Tolima",
        "Parque de la Música",
        "Jardín Botánico Alejandro von Humboldt",
        "Jardín Botánico San Jorge",
        "Parque Museo La Martinica",
        "Santafé de los Guaduales",
        "Fundación Orquídeas del Tolima",
        "Cañón del Combeima",
        "Barrio El Salado",
        "Barrios La Pola y Belén",
        "Plazoleta de los Artesanos",
        "Teatro Tolima",
        "Iglesia El Carmen",
        "Cerro Pan de Azúcar (Mirador)"
    ],
    "hoteles": [
        "Sonesta Hotel Ibagué (5★)",
        "Hotel Estelar Altamira (4★)",
        "Casa Morales Hotel Internacional & Centro de Convenciones (3½★)",
        "Hotel Dann Combeima (4★)",
        "FR Hotel (3★)",
        "Eco Star Hotel (3★)",
        "Hotel Center (3★)",
        "Bahareque Hostal (3★)",
        "Aima Ibagué - Hostel (2★)",
        "Villa Ester Hostel Vereda Cay",
        "Casa Flórez Hotel Campestre",
        "Glamping Akaya (Cañón del Combeima)"
    ],
    "restaurantes": [
        "La Parrilla de Marcos",
        "Rancho Mazorca",
        "Cuzco",
        "Palo Santo"
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = "Lo siento, no tengo una respuesta para eso. Puedes preguntar por sitios turísticos, hoteles o restaurantes en Ibagué."

    if any(palabra in user_input for palabra in ["turismo", "visitar", "atracciones", "lugares", "sitios"]):
        response = "Te recomiendo visitar: " + ", ".join(data["turismo"])
    elif any(palabra in user_input for palabra in ["hotel", "hospedaje", "dormir", "alojamiento"]):
        response = "Aquí tienes algunas opciones de hoteles y hospedajes en Ibagué: " + ", ".join(data["hoteles"])
    elif any(palabra in user_input for palabra in ["restaurante", "comida", "comer", "almorzar", "cenar"]):
        response = "Puedes ir a estos restaurantes en Ibagué: " + ", ".join(data["restaurantes"])

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
