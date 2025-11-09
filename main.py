from flask import Flask, render_template, request, jsonify
from app.controllers.chat_controller import chat_bp

# Crear la app y decirle dónde están las plantillas
app = Flask(__name__, template_folder="app/templates")

# Registrar el Blueprint
app.register_blueprint(chat_bp)

@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Ruta no encontrada"}), 404

if __name__ == "__main__":
    # Render requiere host 0.0.0.0
    app.run(host="0.0.0.0", port=5000)


