from flask import Flask, Response
import os

app = Flask(__name__)

# 🔧 Configuration
PORT = int(os.environ.get("PORT", 5000))
IMAGE_URL = os.environ.get(
    "IMAGE_URL",
    "https://<nomprenom-tp-s3>.s3.amazonaws.com/<nom-img.png>"
)

# 📌 Route principale
@app.route("/")
def index():
    html = generate_html_page()
    return Response(html, mimetype="text/html")

# 📌 Route de santé (bonne pratique)
@app.route("/health")
def health():
    return "OK", 200

# =======================
# Fonctions utilitaires
# =======================

def generate_html_page():
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="UTF-8">
      <title>Application Python Flask | EC2 & S3</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <style>
        body {{
          margin: 0;
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
        }}
        .container {{
          max-width: 720px;
          margin: 60px auto;
          background: #ffffff;
          padding: 30px;
          border-radius: 10px;
          box-shadow: 0 8px 20px rgba(0,0,0,0.1);
          text-align: center;
        }}
        h1 {{
          color: #2c3e50;
        }}
        p {{
          color: #555;
          font-size: 16px;
          line-height: 1.6;
        }}
        img {{
          margin-top: 25px;
          max-width: 100%;
          border-radius: 8px;
          border: 1px solid #ddd;
        }}
        .badge {{
          display: inline-block;
          margin-top: 15px;
          padding: 6px 12px;
          background-color: #27ae60;
          color: white;
          border-radius: 20px;
          font-size: 13px;
        }}
        footer {{
          margin-top: 30px;
          font-size: 13px;
          color: #888;
        }}
      </style>
    </head>

    <body>
      <div class="container">
        <h1>🐍 Application Python Flask 🐍</h1>
        <h2>Aujourd’hui un TP</h2>
        <h2>🚀 demain ton projet peut toucher le monde entier 🚀</h2>

        <p>
          Cette application est déployée sur une instance
          <strong>Amazon EC2</strong> et affiche une image stockée
          dans <strong>Amazon S3</strong>.
        </p>

        <span class="badge">EC2 • Docker • S3 • Flask</span>

        <img src="{IMAGE_URL}" alt="Image stockée dans S3">

        <footer>
          <p>TP Cloud Computing – AWS</p>
        </footer>
      </div>
    </body>
    </html>
    """

# 🚀 Démarrage de l'application
if __name__ == "__main__":
    print("✅ Application Flask démarrée")
    app.run(host="0.0.0.0", port=PORT)
