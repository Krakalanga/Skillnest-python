for i in range(0,101):  #bucle para imprimir los numeros del 0 al 100
    print(i)


for i in range(2,501,2): #bucle para imprimir los numeros multiplos del 2 al 100 
    print(i)


for i in range(1, 101): #bucle que imprime los numeros del 1 al 100, si es divisible por 5 escribe "ice ice" y si es divisible por 10 escribe "baby"
    if(i%10 == 0):
        print("baby")
    elif(i%5== 0):
        print("ice ice")
    else:
        print(i)

#numero gigante

suma= 0
for i in range(0, 500000, 2):
    suma += i

print(suma, " <- Este es el valor de la suma gigante")
    



for i in range(2024, 0, -3): #imprime los numeros en cuenta regresiva de 3 en 3 partiendo desde 2024
    print(i)


#CONTADOR DINAMICO

numInicial = 3
numFinal = 40
multiplo = 3

for i in range(numInicial, numFinal):
    if(i % multiplo == 0):
        print( i, "es multiplo de 3")