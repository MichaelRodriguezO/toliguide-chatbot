from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Configura la API Key desde una variable de entorno
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Instrucciones del asistente
contexto = """
Eres ToliGuide, un asistente turístico especializado en la ciudad de Ibagué, Colombia.
Debes ayudar a los usuarios recomendando lugares turísticos, hoteles, restaurantes y actividades culturales o de naturaleza.
Sitios destacados:
- Turísticos: Plaza de Bolívar, Catedral Primada, Panóptico, Jardín Botánico San Jorge, Cañón del Combeima, Parque Centenario, La Martinica.
- Hoteles: Sonesta, Estelar Altamira, Casa Morales, Dann Combeima, Eco Star.
- Restaurantes: La Parrilla de Marcos, Rancho Mazorca, Palo Santo, Cuzco.
Tu tono debe ser claro, amable y útil.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')

    try:
        # Llamada a OpenAI (usando versión 0.28.1 compatible)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": contexto},
                {"role": "user", "content": user_input}
            ]
        )
        response = completion.choices[0].message["content"].strip()
    except Exception as e:
        response = f"Ocurrió un error: {e}"

    return jsonify({"response": response})

if __name__ == '__main__':
    # Para que funcione en Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
