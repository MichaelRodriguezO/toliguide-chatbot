from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

saludos = ["hola", "wenas", "buenas", "qué más", "holi", "saludos", "empezar", "inicio", "toli", "hey"]

# Google Maps base
def link_maps(nombre):
    return f"📍 Ver en Google Maps: https://www.google.com/maps/search/{'+'.join(nombre.split())}"

info = {
    "introduccion": (
        "¡Hola! Soy ToliGuide, tu asistente turístico de Ibagué 🇨🇴. "
        "Te puedo recomendar sitios turísticos, hoteles y restaurantes. "
        "Escribe 'turismo', 'hoteles' o 'restaurantes' para empezar."
    ),

    "turismo": {
        "historia": {
            "plaza de bolívar y catedral primada": "Corazón histórico de Ibagué, arquitectura clásica y campanas francesas.",
            "parque manuel murillo toro": "Plaza con historia política del Tolima.",
            "museo panóptico": "Antigua cárcel en cruz griega, ahora centro cultural.",
            "barrios la pola y belén": "Casonas coloniales de los primeros pobladores.",
            "teatro tolima": "Joya arquitectónica de 1911 con programación cultural."
        },
        "naturaleza": {
            "jardín botánico san jorge": "Bosque con miradores, senderos y entrada económica.",
            "cañón del combeima": "Ruta natural con termales y miradores al Nevado.",
            "parque museo la martinica": "Cascadas, vistas panorámicas y rappel.",
            "santafé de los guaduales": "Reserva ecológica con senderos y hospedaje.",
            "fundación orquídeas del tolima": "160 especies nativas y recorridos botánicos."
        },
        "cultura": {
            "museo de arte del tolima": "Colección de arte colombiano desde lo precolombino.",
            "museo antropológico ut": "Culturas aborígenes del Tolima.",
            "parque centenario y concha acústica": "Sede de festivales folclóricos.",
            "conservatorio del tolima": "Fundado en 1906, semillero de músicos.",
            "parque de la música": "Escenario musical al aire libre con murales."
        }
    },

    "hoteles": {
        "sonesta hotel ibagué": "Hotel 5★ con piscina, sauna, restaurante y excelente reputación (~9/10).",
        "hotel estelar altamira": "Hotel 4★ con spa, piscina, restaurante, desde $323.000 COP.",
        "casa morales": "Hotel 3½★ ideal para familias, con piscina cubierta.",
        "hotel dann combeima": "Hotel 4★ para familias, con restaurante céntrico.",
        "eco star hotel": "Hotel económico (~$170.000 COP), moderno y bien ubicado."
    },

    "restaurantes": {
        "sonora parrilla bar": "Carnes a la parrilla y platos típicos. Moderno y familiar.",
        "sr. miyagi asian cuisine": "Comida japonesa, tailandesa y china. Internacional.",
        "punta del este restaurante bar": "Parrilla, mariscos, cocina internacional. Vista excelente.",
        "la parrilla de marcos": "Carnes a la brasa y platos tradicionales.",
        "chorilongo": "Choripanes y comida callejera gourmet. Juvenil.",
        "la ricotta": "Cocina italiana, ambiente romántico.",
        "el fogón llanero": "Mamona, carne a la llanera. Rústico y familiar.",
        "restaurante altavista": "Comida colombiana e internacional con vista panorámica.",
        "maria y el mar": "Mariscos y cocina costeña. Sofisticado.",
        "la casona comida típica": "Tamal, lechona y viudo de pescado. Tradicional."
    }
}

# Filtros inteligentes por intención
def filtrar_por_intencion(user_input):
    if "familia" in user_input:
        return (
            "👨‍👩‍👧 Lugares ideales para familias:\n"
            "• Casa Morales\n"
            "• Cañón del Combeima\n"
            "• Jardín Botánico San Jorge\n"
            "• Restaurante Altavista"
        )
    elif "mochilero" in user_input or "hostal" in user_input:
        return (
            "🎒 Recomendado para mochileros:\n"
            "• Eco Star Hotel (económico)\n"
            "• Chorilongo (comida urbana)\n"
            "• Parque Museo La Martinica"
        )
    elif "pareja" in user_input or "romántico" in user_input:
        return (
            "💑 Ideal para parejas:\n"
            "• La Ricotta (restaurante italiano)\n"
            "• Hotel Dann Combeima\n"
            "• Restaurante Altavista (con vista)"
        )
    elif "vista" in user_input:
        return (
            "🌇 Lugares con vista panorámica:\n"
            "• Altavista\n"
            "• La Martinica\n"
            "• Cañón del Combeima"
        )
    elif "marisco" in user_input:
        return (
            "🦐 Restaurantes con mariscos:\n"
            "• Maria y El Mar\n"
            "• Punta del Este Restaurante Bar"
        )
    elif "típico" in user_input or "tamal" in user_input or "lechona" in user_input:
        return (
            "🥘 Comida típica tolimense:\n"
            "• La Casona Comida Típica\n"
            "• La Parrilla de Marcos\n"
            "• El Fogón Llanero"
        )
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = "No entendí tu mensaje. Puedes escribir: turismo, hoteles o restaurantes."

    if any(s in user_input for s in saludos):
        response = info["introduccion"]

    elif "turismo" in user_input:
        response = "🏞 Lugares turísticos por categoría:\n"
        for cat, lugares in info["turismo"].items():
            emoji = {"historia": "📜", "naturaleza": "🌿", "cultura": "🎭"}[cat]
            response += f"\n{emoji} {cat.capitalize()}:\n• " + "\n• ".join(lugares.keys()) + "\n"

    elif "hotel" in user_input:
        response = "🛌 Hoteles recomendados:\n• " + "\n• ".join(info["hoteles"].keys())

    elif "restaurante" in user_input or "comida" in user_input:
        response = "🍽 Restaurantes destacados:\n• " + "\n• ".join(info["restaurantes"].keys())

    else:
        # Filtros inteligentes por tipo de viajero o preferencia
        filtro = filtrar_por_intencion(user_input)
        if filtro:
            response = filtro
        else:
            # Buscar coincidencias por palabra clave
            encontrado = False
            for categoria in ["turismo", "hoteles", "restaurantes"]:
                if categoria == "turismo":
                    for subcat in info["turismo"].values():
                        for nombre, descripcion in subcat.items():
                            if any(p in user_input for p in nombre.split()):
                                response = f"{nombre.title()}:\n{descripcion}\n{link_maps(nombre)}"
                                encontrado = True
                                break
                        if encontrado:
                            break
                else:
                    for nombre, descripcion in info[categoria].items():
                        if any(p in user_input for p in nombre.split()):
                            response = f"{nombre.title()}:\n{descripcion}\n{link_maps(nombre)}"
                            encontrado = True
                            break
                if encontrado:
                    break

    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
