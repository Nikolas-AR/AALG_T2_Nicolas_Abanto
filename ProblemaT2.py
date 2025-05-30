import random
import math

def distancia (origen):
    x=origen[0]
    y=origen[1]
    return math.sqrt(x**2 + y**2)

def coordLejana(matriz):
    if len(matriz) == 1: 
        x, y = matriz [0]
        if x>0 and y<0:
            return matriz[0]
        else:
            return []
        
    medio = len(matriz) // 2

    izq = []
    der = []

    for i in range(medio):
        izq.append(matriz[i])

    for i in range(medio, len(matriz)):
        der.append(matriz[i])

    result_izq = coordLejana(izq) 
    result_der = coordLejana(der)

    return Combinar(result_izq,  result_der)


def Combinar(izq,der):
    if izq and der:
        if distancia(izq) > distancia(der):
            return izq
        else:
            return der
    elif izq:
        return izq
    elif der:
        return der
    else: 
        return []
        

n = int(input("¿Cuántos pares de coordenadas deseas generar? "))
matriz = []
for i in range(n):
    x = random.randint(-81, 81)
    y = random.randint(-81, 81)
    matriz.append([x,y])
    
print("\nCoodenadas generadas: ")
for par in matriz:
    print(par)

resultado = coordLejana(matriz)

print("-----------------------------------------------------")
print("La coordenada más alejada del origen es: ", resultado)   
print("Distancia al origen: ", round(distancia(resultado), 2)) 