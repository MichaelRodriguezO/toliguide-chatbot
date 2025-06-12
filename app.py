from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Configurar la API Key de OpenAI desde una variable de entorno
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Contexto para que el modelo sepa cómo debe comportarse
contexto = """
Eres ToliGuide, un asistente turístico experto en Ibagué, Colombia.
Puedes recomendar lugares turísticos, hoteles, restaurantes, zonas de naturaleza, barrios tradicionales,
y dar consejos para turistas nacionales o extranjeros.
Aquí algunos lugares destacados:
- Turísticos: Plaza de Bolívar, Catedral Primada, Panóptico, Jardín Botánico San Jorge, Parque Museo La Martinica, Cañón del Combeima.
- Hoteles: Sonesta, Hotel Estelar Altamira, Casa Morales, Hotel Dann Combeima, Eco Star Hotel.
- Restaurantes: La Parrilla de Marcos, Rancho Mazorca, Palo Santo, Cuzco.
Tu tono debe ser amigable, claro y útil.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')

    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # o "gpt-4" si tienes acceso
            messages=[
                {"role": "system", "content": contexto},
                {"role": "user", "content": user_input}
            ]
        )

        response = completion.choices[0].message.content.strip()
    except Exception as e:
        response = f"Ocurrió un error: {str(e)}"

    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
