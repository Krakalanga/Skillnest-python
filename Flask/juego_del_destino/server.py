from flask import Flask, render_template, request, redirect, session

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
    return render_template('futuro.html', nombre = session['nombre'], numero = session['numero'], lugar = session['lugar'], comida = session['comida'])

@app.route('/volver')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)