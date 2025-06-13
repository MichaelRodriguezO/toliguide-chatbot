from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Lista de saludos reconocidos
saludos = ["hola", "buenas", "wenas", "qué más", "holi", "saludos", "buen día", "buenas tardes", "empezar", "inicio", "toli", "hey"]

# Base de datos turística
info = {
    "introduccion": (
        "¡Hola! Soy ToliGuide, tu asistente turístico de Ibagué 🇨🇴. "
        "Puedo mostrarte los mejores lugares para visitar, hoteles y restaurantes. "
        "Escribe 'turismo', 'hoteles' o 'restaurantes' para comenzar."
    ),
    "turismo": {
        "plaza de bolívar y catedral primada": "Corazón histórico de Ibagué. La Catedral destaca por su estilo ecléctico, reloj suizo de 1929 y campanas francesas.",
        "parque centenario y concha acústica": "Pulmón verde y escenario de festivales locales como el Festival Folclórico.",
        "parque manuel murillo toro": "Plaza central con historia política, remodelada en 2013 y 2018.",
        "plazoleta darío echandía": "Escenario cultural con tarima para eventos musicales y públicos.",
        "museo de arte del tolima": "Colección de 500 obras colombianas, desde arte precolombino hasta contemporáneo.",
        "museo panóptico": "Antigua cárcel en cruz griega, ahora centro cultural y símbolo patrimonial.",
        "museo antropológico ut": "30 años de investigación sobre culturas aborígenes del Tolima.",
        "conservatorio del tolima": "Fundado en 1906, ícono arquitectónico y semillero de músicos.",
        "parque de la música": "Parque temático al aire libre con murales y conciertos educativos.",
        "jardín botánico alejandro von humboldt": "Ecosistemas andinos para caminatas educativas.",
        "jardín botánico san jorge": "60 ha de bosque subandino con miradores y senderos.",
        "parque museo la martinica": "Vistas de la ciudad y actividades como rappel y cascadas.",
        "santafé de los guaduales": "Reserva ecológica con senderos, temazcal y hospedaje.",
        "fundación orquídeas del tolima": "160 especies propias y senderos botánicos.",
        "cañón del combeima": "Ruta natural con termales, miradores y senderismo al Nevado.",
        "barrio el salado": "Encanto tradicional tolimense y buena gastronomía.",
        "barrios la pola y belén": "Casonas coloniales que evocan los primeros pobladores.",
        "plazoleta de los artesanos": "Ideal para comprar artesanías hechas a mano.",
        "teatro tolima": "Joya arquitectónica de 1911, con programación cultural.",
        "iglesia el carmen": "Construcción del siglo XX con materiales de EE.UU.",
        "cerro pan de azúcar": "Mirador con imagen de la Virgen, destino de peregrinación."
    },
    "hoteles": {
        "sonesta hotel ibagué": "Hotel 5★ con piscina, sauna, gimnasio y excelente reputación (~9/10).",
        "hotel estelar altamira": "Hotel 4★ con spa, piscina, restaurante, desde $323.000 COP.",
        "casa morales": "Hotel 3½★ ideal para negocios y eventos, con piscina cubierta.",
        "hotel dann combeima": "Hotel 4★ para familias, con restaurante y buena ubicación.",
        "fr hotel": "Hotel 3★ con buena atención, precios entre $180.000 COP.",
        "eco star hotel": "Hotel 3★ moderno y económico (~$170.000 COP).",
        "hotel center": "Ubicación céntrica y buena calidad-precio.",
        "bahareque hostal": "Económico y limpio, cerca del centro (~US$33).",
        "aima ibagué - hostel": "Estilo mochilero, ambiente juvenil y WiFi gratis.",
        "villa ester hostel": "Ambiente tranquilo, top 1 en Booking.",
        "casa flórez hotel campestre": "Ambiente campestre, ideal para familias y parejas.",
        "glamping akaya": "Cabañas tipo glamping en el Cañón del Combeima."
    },
    "restaurantes": {
        "la parrilla de marcos": "Especialidad en carnes a la parrilla, ambiente familiar.",
        "rancho mazorca": "Comida típica tolimense con ambiente rústico.",
        "cuzco": "Fusión peruana-colombiana con ambiente elegante.",
        "palo santo": "Gastronomía gourmet colombiana con toque moderno."
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = "No entendí tu mensaje. Puedes escribir: turismo, hoteles o restaurantes."

    # Saludos reconocidos
    if any(saludo in user_input for saludo in saludos):
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
        # Buscar por palabra clave o error parcial
        for categoria in ["turismo", "hoteles", "restaurantes"]:
            for nombre, descripcion in info[categoria].items():
                if any(palabra in user_input for palabra in nombre.split()):
                    response = f"{nombre.title()}:\n{descripcion}"
                    break
            if response.startswith(nombre.title()):
                break

    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
