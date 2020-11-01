def maxi(*l): # l es un array
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1,len(l)):
        if l[ix] > m:
            m = l[ix]
    
    return m


def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1,len(l)):
        if l[ix] < m:
            m = l[ix]    
    
    return m



def media(*l):
    if len(l) == 0:
        return 0
    
    suma = 0
    for valor in l:
        suma += valor
    
    return suma / len(l)


funciones = {'max': maxi, 'min': mini, 'med': media} # diccionario con los nombres de las funciones

# Creamos una función que devuelva una de las 3 funciones anteriores usando el diccionario.
def returnF(nombre):
    if nombre.lower() in funciones.keys():
        return funciones[nombre]
    
    return None

returnF('max')(1,3,-1,15,9) # invocamos una función de primer nivel que nos devuelve una funcion,
#cual? la que la pedimos.. en este caso MAXI
# y le damos sus parámetros para que se ejecute.