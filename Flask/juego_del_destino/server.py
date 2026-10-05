from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = '123'
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/futuro', methods=['POST'])
def futuro():
    if 'nombre' not in session:
        session['nombre'] = request.form.get('nombre')
    if 'numero' not in session:
        session['numero'] = request.form.get('numero')
    if 'lugar' not in session:
        session['lugar'] = request.form.get('lugar')
    if 'comida' not in session:
        session['comida'] = request.form.get('comida')
    if 'profesion' not in session:
        session['profesion'] = request.form.get('profesion')
    if random.randint(0,1) == 1:
        return render_template('futuroMalo.html', nombre = session['nombre'], numero = session['numero'], lugar = session['lugar'], comida = session['comida'], profesion = session['profesion'])
    return render_template('futuro.html', nombre = session['nombre'], numero = session['numero'], lugar = session['lugar'], comida = session['comida'], profesion = session['profesion'])

@app.route('/volver')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)