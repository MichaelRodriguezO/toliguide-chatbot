from flask import Flask, request, jsonify, render_template
import os
import difflib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    return jsonify({"response": "Bot funcional con toda la base de datos de Ibagué. 🏞️🍽️🛌"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
