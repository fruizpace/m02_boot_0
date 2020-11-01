from functools import reduce

lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista) # map aplica la función que le des a cada elemento

listaPares = filter(lambda x: x%2 == 0, lista) # filter usa la condición true/false que sale de la función anónima

sumatorio = reduce(lambda x, y: x+y, lista)
# reduce: x es un acumulador y es el valor que me dará reduce.
# en "y" entran los elementos de la lista.

suma100 = reduce(lambda x, y: x+y, range(101))