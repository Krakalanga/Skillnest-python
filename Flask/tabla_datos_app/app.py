from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de plataformas digitales
datos = [
   {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia", "logo": "spotify.png", "color": "#24df66"},
   {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU.", "logo": "netflix.png", "color": "#000000"},
   {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU.", "logo": "youtube.png", "color": "#FF0000"},
   {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU.", "logo": "twitch.png", "color": "#6b45b5"},
   {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China", "logo": "tiktok.png", "color": "#000000"},
   {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU.", "logo": "instagram.png", "color": "radial-gradient(circle at 30% 110%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%)"},
   {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU.", "logo": "discord.png", "color": "#5865F2"},
]

# Ruta para mostrar la tabla con datos
@app.route('/')
def home():
   return render_template('tabla.html', datos = datos)

if __name__ == "__main__":
   app.run(debug=True)