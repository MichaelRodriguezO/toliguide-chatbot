from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Diccionario con toda la información estructurada
info = {
    "introduccion": (
        "¡Hola! Soy ToliGuide, tu asistente turístico de Ibagué 🇨🇴. "
        "Puedo mostrarte los mejores lugares para visitar, hoteles y restaurantes. "
        "Escribe 'turismo', 'hoteles' o 'restaurantes' para comenzar."
    ),
    "turismo": {
        "Plaza de Bolívar y Catedral Primada": "Corazón histórico de Ibagué. La Catedral destaca por su estilo ecléctico, reloj suizo de 1929 y campanas francesas.",
        "Parque Centenario y Concha Acústica": "Pulmón verde y escenario de festivales locales como el Festival Folclórico.",
        "Parque Manuel Murillo Toro": "Plaza central con historia política, remodelada en 2013 y 2018.",
        "Plazoleta Darío Echandía": "Escenario cultural con tarima para eventos musicales y públicos.",
        "Museo de Arte del Tolima": "Colección de 500 obras colombianas, desde arte precolombino hasta contemporáneo.",
        "Museo Panóptico": "Antigua cárcel en cruz griega, ahora centro cultural y símbolo patrimonial.",
        "Museo Antropológico UT": "30 años de investigación sobre culturas aborígenes del Tolima.",
        "Conservatorio del Tolima": "Fundado en 1906, ícono arquitectónico y semillero de músicos.",
        "Parque de la Música": "Parque temático al aire libre con murales y conciertos educativos.",
        "Jardín Botánico Alejandro von Humboldt": "Ecosistemas andinos para caminatas educativas.",
        "Jardín Botánico San Jorge": "60 ha de bosque subandino con miradores y senderos.",
        "Parque Museo La Martinica": "Vistas de la ciudad y actividades como rappel y cascadas.",
        "Santafé de los Guaduales": "Reserva ecológica con senderos, temazcal y hospedaje.",
        "Fundación Orquídeas del Tolima": "160 especies propias y senderos botánicos.",
        "Cañón del Combeima": "Ruta natural con termales, miradores y senderismo al Nevado.",
        "Barrio El Salado": "Encanto tradicional tolimense y buena gastronomía.",
        "Barrios La Pola y Belén": "Casonas coloniales que evocan los primeros pobladores.",
        "Plazoleta de los Artesanos": "Ideal para comprar artesanías hechas a mano.",
        "Teatro Tolima": "Joya arquitectónica de 1911, con programación cultural.",
        "Iglesia El Carmen": "Construcción del siglo XX con materiales de EE.UU.",
        "Cerro Pan de Azúcar": "Mirador con imagen de la Virgen, destino de peregrinación."
    },
    "hoteles": {
        "Sonesta Hotel Ibagué": "Hotel 5★ con piscina, sauna, gimnasio y excelente reputación (~9/10).",
        "Hotel Estelar Altamira": "Hotel 4★ con spa, piscina, restaurante, desde $323.000 COP.",
        "Casa Morales": "Hotel 3½★ ideal para negocios y eventos, con piscina cubierta.",
        "Hotel Dann Combeima": "Hotel 4★ para familias, con restaurante y buena ubicación.",
        "FR Hotel": "Hotel 3★ con buena atención, precios entre $180.000 COP.",
        "Eco Star Hotel": "Hotel 3★ moderno y económico (~$170.000 COP).",
        "Hotel Center": "Ubicación céntrica y buena calidad-precio.",
        "Bahareque Hostal": "Económico y limpio, cerca del centro (~US$33).",
        "Aima Ibagué - Hostel": "Estilo mochilero, ambiente juvenil y WiFi gratis.",
        "Villa Ester Hostel": "Ambiente tranquilo, top 1 en Booking.",
        "Casa Flórez Hotel Campestre": "Ambiente campestre, ideal para familias y parejas.",
        "Glamping Akaya": "Cabañas tipo glamping en el Cañón del Combeima."
    },
    "restaurantes": {
        "La Parrilla de Marcos": "Especialidad en carnes a la parrilla, ambiente familiar.",
        "Rancho Mazorca": "Comida típica tolimense con ambiente rústico.",
        "Cuzco": "Fusión peruana-colombiana con ambiente elegante.",
        "Palo Santo": "Gastronomía gourmet colombiana con toque moderno."
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = "No entendí tu mensaje. Puedes escribir: turismo, hoteles o restaurantes."

    if any(palabra in user_input for palabra in ["hola", "inicio", "empezar", "toli"]):
        response = info["introduccion"]

    elif "turismo" in user_input:
        lista = "\n• " + "\n• ".join(info["turismo"].keys())
        response = "🏞 Lugares turísticos recomendados:\n" + lista

    elif "hotel" in user_input:
        lista = "\n• " + "\n• ".join(info["hoteles"].keys())
        response = "🛌 Hoteles destacados en Ibagué:\n" + lista

    elif "restaurante" in user_input or "comida" in user_input:
        lista = "\n• " + "\n• ".join(info["restaurantes"].keys())
        response = "🍽 Restaurantes recomendados:\n" + lista

    else:
        # Buscar lugar específico
        for categoria in ["turismo", "hoteles", "restaurantes"]:
            for nombre, descripcion in info[categoria].items():
                if nombre.lower() in user_input:
                    response = f"{nombre}:\n{descripcion}"
                    break

    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

