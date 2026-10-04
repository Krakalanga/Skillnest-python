from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = '12345'

vecesReiniciado = 0

#el codigo de python y el html lo hice a mano pero el css fue vibecodeado


@app.route('/')
def home():
    session['visitas'] = session.get('visitas', 0) + 1 #cada vez que se visita la ruta raiz aumenta el valor de las visitas en 1
    return render_template('index.html', cantidad = session['visitas'], reiniciado = vecesReiniciado)

@app.route('/destruir_sesion')
def borrar():
    session.clear() #limpia la sesion
    return redirect('/')
    
@app.route('/aumentar2') #ruta para aumentar en +2 las visitas
def aumentar():
    session['visitas'] = session.get('visitas', 0) + 1 #le sumo 1 porque al redirigir ya suma otra, haciendo que sumen en total 2
    return redirect('/')

@app.route('/reiniciar0') #contador de veces reiniciado
def reiniciar():
    global vecesReiniciado #declaro que la variable es global
    vecesReiniciado += 1
    session['visitas'] = -1
    return redirect('/')

@app.route('/aumentarCantidad', methods=['POST'])
def aumentarCantidad():
    session['visitas'] = session.get('visitas', 0) + int(request.form.get('numero', 0)) - 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)