########### Tipo de dato ##############
# String
estring = 'Comillas simple'
oracion = "Hola esto es una oracion"

# Entero
entero = 20
#Float
decimal = 20.2
#Números complejos
complejo = 1j
#print(estring,oracion,entero,decimal,complejo)

#Lista 
lista = [1,2,2,3]

#Agregar elemento al final
lista.append(4)
print(lista)


# copiar elemento a otra variable
lista2 = lista.copy()
print(lista2)

#Limpiar elementos de la lista
lista.clear()
print(lista)

#Contar elemetos que se repiten de la lista
print(lista2.count(2))

#Obtener el nuemro de elemetos de una lista
print(len(lista2))

#El primer elemento de una lista esta en la posicion 0
print(lista2[0])
#Imprimir el último valor de una lista
print(lista2[len(lista2)-1])

#Eliminar elemento de la lista
lista2.pop()
print(lista2)

#Elimiar un elemento especifico de la lista
lista2.remove(2)
print(lista2)

#Ordenar elementos de una lista
lista2.reverse()
print(lista2)