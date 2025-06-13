from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Lista de saludos que activa el mensaje de bienvenida
saludos = ["hola", "wenas", "buenas", "qué más", "holi", "saludos", "buen día", "empezar", "inicio", "toli", "hey"]

# Base de datos del chatbot
info = {
    "introduccion": (
        "¡Hola! Soy ToliGuide, tu asistente turístico de Ibagué 🇨🇴. "
        "Te puedo recomendar sitios turísticos, hoteles y restaurantes. "
        "Escribe 'turismo', 'hoteles' o 'restaurantes' para empezar."
    ),

    "turismo": {
        "historia": {
            "plaza de bolívar y catedral primada": "Corazón histórico de Ibagué, arquitectura clásica y campanas francesas.",
            "parque manuel murillo toro": "Plaza central con historia política.",
            "museo panóptico": "Antigua cárcel en cruz griega, ahora centro cultural.",
            "barrios la pola y belén": "Casonas coloniales de los primeros pobladores.",
            "teatro tolima": "Joya arquitectónica de 1911 con programación cultural."
        },
        "naturaleza": {
            "jardín botánico san jorge": "60 ha de bosque con miradores, senderos y acceso económico.",
            "cañón del combeima": "Ruta natural con termales, miradores y acceso al Nevado.",
            "parque museo la martinica": "Mirador, cascadas, rappel y vistas panorámicas.",
            "santafé de los guaduales": "Reserva ecológica con senderos, temazcal y hospedaje.",
            "fundación orquídeas del tolima": "160 especies propias, recorridos botánicos."
        },
        "cultura": {
            "museo de arte del tolima": "Colección de arte colombiano desde lo precolombino.",
            "museo antropológico ut": "Culturas aborígenes del Tolima.",
            "parque centenario y concha acústica": "Sede de festivales folclóricos.",
            "conservatorio del tolima": "Fundado en 1906, semillero de músicos.",
            "parque de la música": "Escenario musical al aire libre con murales y esculturas."
        }
    },

    "hoteles": {
        "sonesta hotel ibagué": "Hotel 5★ con piscina, sauna, gimnasio y excelente reputación (~9/10).",
        "hotel estelar altamira": "Hotel 4★ con spa, piscina, restaurante, desde $323.000 COP.",
        "casa morales": "Hotel 3½★ ideal para negocios y eventos, con piscina cubierta.",
        "hotel dann combeima": "Hotel 4★ para familias, con restaurante y buena ubicación.",
        "eco star hotel": "Hotel económico (~$170.000 COP), moderno y bien ubicado."
    },

    "restaurantes": {
        "sonora parrilla bar": "Carnes a la parrilla, platos típicos. Ambiente moderno y familiar.",
        "sr. miyagi asian cuisine": "Comida asiática (japonesa, tailandesa, china). Sabores internacionales.",
        "punta del este restaurante bar": "Parrilla, mariscos, cocina internacional. Vista y ambiente elegante.",
        "la parrilla de marcos": "Carnes a la brasa y platos típicos. Muy tradicional.",
        "chorilongo": "Choripanes y comida callejera gourmet. Popular entre jóvenes.",
        "la ricotta": "Cocina italiana, pizzas artesanales. Ambiente romántico.",
        "el fogón llanero": "Comida del Llano (mamona, carne a la llanera). Rústico y familiar.",
        "restaurante altavista": "Cocina colombiana e internacional. Vista panorámica.",
        "maria y el mar": "Mariscos y cocina costeña. Ambiente sofisticado.",
        "la casona comida típica": "Tamal, lechona y viudo de pescado. Comida tolimense tradicional."
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = "Lo siento, no entendí tu mensaje. Puedes escribir: turismo, hoteles o restaurantes."

    # Reconocimiento de saludos
    if any(s in user_input for s in saludos):
        response = info["introduccion"]

    elif "turismo" in user_input:
        response = "🏞 Lugares turísticos por categoría:\n"
        for categoria, lugares in info["turismo"].items():
            emoji = {"historia": "📜", "naturaleza": "🌿", "cultura": "🎭"}.get(categoria, "•")
            response += f"\n{emoji} {categoria.capitalize()}:\n" + "\n• " + "\n• ".join(lugares.keys()) + "\n"

    elif "hotel" in user_input:
        response = "🛌 Hoteles recomendados:\n• " + "\n• ".join(info["hoteles"].keys())

    elif "restaurante" in user_input or "comida" in user_input:
        response = "🍽 Restaurantes destacados:\n• " + "\n• ".join(info["restaurantes"].keys())

    else:
        # Buscar coincidencias por palabra clave en todos los nombres
        encontrado = False
        for categoria in ["turismo", "hoteles", "restaurantes"]:
            if categoria == "turismo":
                for subcat in info["turismo"].values():
                    for nombre, descripcion in subcat.items():
                        if any(palabra in user_input for palabra in nombre.split()):
                            response = f"{nombre.title()}:\n{descripcion}"
                            encontrado = True
                            break
                    if encontrado:
                        break
            else:
                for nombre, descripcion in info[categoria].items():
                    if any(palabra in user_input for palabra in nombre.split()):
                        response = f"{nombre.title()}:\n{descripcion}"
                        encontrado = True
                        break
            if encontrado:
                break

    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
