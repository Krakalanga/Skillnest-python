from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = '123'



def nuevo_juego():
    session['num'] = random.randint(1, 10)
    session['intentos'] = 0
    session.pop('mensaje', None)
    session.pop('ganado', None)

@app.route('/')
def home():
    if 'num' not in session:
        nuevo_juego()
    return render_template(
        'index.html',
        intentos=session.get('intentos', 0),
        mensaje=session.get('mensaje'),
        ganado=session.get('ganado', False),
    )

@app.route('/adivinar', methods=['POST'])
def adivinar():
    intento = request.form.get('numero', type=int)
    secreto = session.get('num')

    if intento is None:
        session['mensaje'] = 'Ingresa un número válido.'
        session['ganado'] = False
        return redirect('/')

    if intento == secreto:
        session['intentos'] += 1
        session['mensaje'] = f' ¡Adivinaste! El número era {secreto}. Lo lograste en {session["intentos"]} intento(s).'
        session['ganado'] = True
        
        session['num'] = random.randint(1, 10) #se genera un nuevo numero
        session['intentos'] = 0
    else:
        session['intentos'] += 1
        session['ganado'] = False
        if intento < secreto:
            session['mensaje'] = 'Muy bajo :( intenta con un número mayor.'
        else:
            session['mensaje'] = 'Muy alto :(  intenta con un número menor.'

    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)