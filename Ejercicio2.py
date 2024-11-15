#2.1
nom = input('¿Como te llamas? (Nombre Apellido): ')
nom = nom.split(' ')
print(nom[0])

#2.2
palabra = input('Dime una palbra: ')
vocal = input('Dime una vocal: ')
vocal = vocal.upper()
word = vocal.replace(palabra)