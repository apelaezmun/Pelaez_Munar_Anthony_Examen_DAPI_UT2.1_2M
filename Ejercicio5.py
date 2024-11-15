#5.1
def area_cuadrado(lado):
    return lado **2
num = float(input('Dime cuanto mide 1 lado del cuadrado: '))
print(area_cuadrado(num))

#5.2
def mayor_de_tres(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
print(mayor_de_tres(1, 8, 4))