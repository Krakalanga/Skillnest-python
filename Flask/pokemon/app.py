from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de Pokémon
pokedex = [
   {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen" : "bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
   {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "Charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
   {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "Squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
   {"id": 25, "nombre": "Pikachu", "tipo": "Electrico", "imagen": "Pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
   {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "Jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
   {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "Meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
   {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
   {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "Gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
   {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "Onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
   {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "Snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]


# Ruta para mostrar todos los Pokémon
@app.route('/')
def pokemon():
   return render_template('pokemon.html', pokedex = pokedex)
# Ruta para mostrar un Pokémon por nombre
@app.route('/<pokemon>')
def pokemonPorNombre(pokemon: str):
   pokemon_encontrado = None
   for p in pokedex:
      if p["nombre"].lower() == pokemon.lower():
         pokemon_encontrado = p
         return render_template('pokemon_unico.html', x = pokemon_encontrado)
      
   return render_template("404.html", mensaje=pokemon)

# Ruta para mostrar un Pokémon por número de ID en la Pokédex
@app.route('/<int:id>')
def idPokemon(id):
   pokemon = None
   for p in pokedex:
      if p["id"] == id:
         return render_template('pokemon_unico.html', x = p)
  
   return render_template("404.html", mensaje = id)


# Ruta para mostrar una cantidad específica de Pokémon

@app.route('/cantidad/<int:cantidad>')
def cantidadpokemon(cantidad):
   valor = 0
   pokedex_nueva = []
   while valor < cantidad and valor < len(pokedex):
      pokedex_nueva.append(pokedex[valor])
      valor += 1
   return render_template('cantidadPokemones.html', pokedex = pokedex_nueva)


if __name__ == "__main__":
   app.run(debug=True)