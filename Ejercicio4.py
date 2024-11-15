#4.1
lista = []
paises = input('Dime tres paises que te gustaria visitar (pais, pais, pais): ')
lista.append(paises)
for i in range(len(lista)):
    print('Me gustaria visitar', lista[i])

#4.2
nums = (input('Dame una lista de numeros enteros (x, x, x,...): '))
listaNum = [nums]
listaNum.sort()
listaNum.reverse()
print(listaNum)