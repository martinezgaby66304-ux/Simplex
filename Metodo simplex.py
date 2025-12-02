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