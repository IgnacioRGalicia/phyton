Sample = '3, 5, 7, 23'
lista = list()
tupla = tuple()
numbers = Sample.split(', ')
for num in numbers:
    lista = lista.append(num)
print(lista)