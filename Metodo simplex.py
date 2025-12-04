import numpy as np

class Simplex:
    def __init__(self, funcion, restriccion, tipo):
        self.funcion = funcion
        self.restriccion = restriccion
        self.tipo = tipo

def Mostrar_tipo(tipo):
    if tipo == 1:
        return "Maximización"
    elif tipo == 2:
        return "Minimización"
    
def convertir_a_maximizacion_minimizacion(tipo, funcion, restriccion):
    funcion_convertida = []
    if tipo == 1:
        for coeficiente in funcion:
            funcion_convertida.append(coeficiente)
    elif tipo == 2:
        for coeficiente in funcion:
            funcion_convertida.append(-coeficiente)
            
    return funcion_convertida, restriccion

print("¿Qué tipo de problema quieres resolver?")
print("1 = Maximización")
print("2 = Minimización")
tipo = int(input("Ingrese el tipo de problema: "))

funcion = [float(x) for x in input("Ingrese los coeficientes de la función objetivo separados por espacios: ").split()]

restricciones = []
limites = []
n = int(input("Ingrese el número de restricciones: "))

for i in range(n):
    coeficientes = [float(x) for x in input(f"Ingrese los coeficientes de la restricción {i+1} separados por espacios: ").split()]
    restricciones.append(coeficientes)
    limite = float(input(f"Ingrese el límite de la restricción {i+1}: "))
    limites.append(limite)