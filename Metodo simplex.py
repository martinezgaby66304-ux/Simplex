import numpy as np
import scipy.optimize as opt

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

Simplex = Simplex(funcion, restricciones, tipo)
A = np.array(restricciones)
limites = np.array(limites)

if tipo == 1:
       c = -np.array(funcion)
else:
       c = np.array(funcion)

res = opt.linprog(c, A_ub=A, b_ub=limites, method="simplex")

print("RESULTADOS")
if res.success:
    if tipo == 1:
        print("Problema de Maximización")
        print("Valores óptimos de las variables:", res.x)
        print("Valor óptimo Z:", -res.fun)
    else:
        print("Problema de Minimización")
        print("Valores óptimos de las variables:", res.x)
        print("Valor óptimo Z:", res.fun)

