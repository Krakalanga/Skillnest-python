#MATRIZ

matriz = [ [10, 15, 20], [3, 7, 14] ]
print(matriz, "valor original")
matriz[1][0] = 6 #cambiar valor 3 por un 6
print(f"{matriz}, valor cambiado")


cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

print(cantantes)
cantantes[0]["nombre"] = "Enrique Martin Morales" #cambiar ricky martin por enrique martin morales
print(cantantes, "Nombre cambiado")



ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

print(ciudades["México"])
ciudades["México"][2] = "Monterrey" #cambiar cancún por monterrey
print(ciudades["México"], "valor cambiado")


coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

print(coordenadas, "valor original")

coordenadas[0]["latitud"] = 9.9355431 #valor nuevo en latitud

print(coordenadas, "valor cambiado")


#Parte 2 de core

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario(lista):
    for x in range(len(lista)): #bucle para mostrar cada elemento de la lista iterando el indice
        print(lista[x])
        


iterarDiccionario(cantantes)

def iterarDiccionario2(llave, lista):
    for x in lista: #recorre la lista
        print(x[llave]) #imprime el valor de la llave de cada elemento en la lista
iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)


costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def imprimirinformacion(diccionario):
    for x in diccionario:
        print(len(diccionario[x]), x.upper()) #imprime el largo de la lista y la llave en mayuscula
        for elemento in diccionario[x]:
            print(elemento) #recorre la lista de la llave

imprimirinformacion(costa_rica)
