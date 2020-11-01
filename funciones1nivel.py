# Tenemos tres funciones
def normal(x):
    return x

def cuadrado(x):
    return x * x

def cubo(x):
    return x**3

# y ahora creamos una función de primer nivel en el que uno de sus parámetros es una función a elegir:
def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i) # aquí entra una de las funciones que indiquemos: normal o cuadrado
    
    return resultado


if __name__ == '__main__': # significa que la función se está ejecutando en esta consola. Si la
    #ejecuta como módulo en __name__ tendrá el nombre del script "funciones1nivel".
    print(sumaTodos(3, cuadrado))
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cubo))
else:
    print(__name__)


