from flask import Flask, render_template, request, jsonify
from app.controllers.chat_controller import chat_bp

app = Flask(__name__, template_folder="app/templates")

# Registrar Blueprint del chat
app.register_blueprint(chat_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


