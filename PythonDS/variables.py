#Variables, tipos y operadores
a, b, c = 10, 20, 30
promedio = (a + b + c) / 3
print(promedio)

int_num = 4

print(float(int_num))

base = int(input("Ingresa la base"))
altura = int(input("Ingresa la altura"))

res = (base * altura) / 2

print(res)

x = 5
y = 10

x = x + y   # x ahora vale 15 (suma de ambos)
y = x - y   # y ahora vale 5  (el valor original de x)
x = x - y   # x ahora vale 10 (el valor original de y)

print(a, b)  # salida: 10 5


i = 5
j = 10

i, j = j, i

print(a, b)  # salida: 10 5


num = int(input("Ingresa un numero"))

if num % 2 == 0:
    print("par")
else:
    print("inpar")


sentence = "Hola mundo cruel"

print(sentence[:3])
print(sentence[-3:])


def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

lista_primos = [numero for numero in range(2, 101) if es_primo(numero)]
print(lista_primos)

# Dado un string numérico "1234", conviértelo a entero y súmale 6.

qty = "1234"

res = int(qty) + 6

print(res)