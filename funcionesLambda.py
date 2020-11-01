from funciones1nivel import sumaTodos 

print(sumaTodos(3, lambda x: x**3))
# con lambda creas una función anónima, suelen ser sencillas y la usarás poco

# otra opción
doble = lambda x: x**3 # no es necesario indicar return
print(sumaTodos(3, doble))
