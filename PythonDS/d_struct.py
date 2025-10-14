# 🧰 2. Listas y diccionarios
# Crea una lista con 10 números. Obtén el máximo y mínimo sin usar max() ni min().
# Invierte una lista sin usar .reverse() ni slicing.
# Cuenta cuántas veces aparece cada número en una lista (usa un diccionario).
# Dada una lista de nombres, elimina los duplicados manteniendo el orden original.
# Une dos listas elemento a elemento en una lista de tuplas.
# Dado un diccionario con productos y precios, obtén el producto más caro.
# Crea un diccionario con claves del 1 al 10 y valores que sean sus cuadrados.
# Ordena un diccionario por sus valores de forma ascendente.
# Convierte una lista de tuplas [("a",1),("b",2)] en un diccionario.
# Elimina todas las claves cuyo valor sea menor que 50.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def min_max(arr):
    left = 0
    right = len(arr) -1

    while left < right:
        print(left)
        print(right)
    
#     while izquierda < derecha:
#         suma_actual = arr[izquierda] + arr[derecha]

#         if suma_actual == objetivo:
#             return arr[izquierda], arr[derecha]
#         elif suma_actual < objetivo:
#             izquierda += 1
#         else: # suma_actual > objetivo
#             derecha -= 1

min_max(l)

# 🔁 3. Bucles y condicionales
# Imprime los números del 1 al 100, pero sustituye:
# “Fizz” si es múltiplo de 3,
# “Buzz” si es múltiplo de 5,
# “FizzBuzz” si es múltiplo de ambos.
# Calcula la suma de todos los números pares del 1 al 50.
# Cuenta cuántas vocales tiene una palabra ingresada.
# Dibuja con print() un triángulo de asteriscos de altura n.
# Pide al usuario números hasta que ingrese uno negativo, luego muestra la suma total.
# Recorre un diccionario e imprime solo las claves cuyos valores sean pares.
# Recorre una lista de palabras e imprime solo las que empiecen con vocal.

# 🧩 4. Funciones
# Escribe una función que reciba un número y devuelva True si es primo.
# Escribe una función que reciba una lista y devuelva otra con los elementos únicos.
# Crea una función que reciba una lista y devuelva su promedio.
# Define una función que reciba una cadena y devuelva la misma cadena sin vocales.
# Escribe una función que reciba una palabra y devuelva si es palíndromo.
# Crea una función que reciba dos listas y devuelva una con los elementos comunes.
# Crea una función que reciba un número entero n y devuelva una lista con los números del 1 a n al cuadrado.

# 🔁 5. Recursión
# Calcula el factorial de un número usando recursión.
# Calcula el n-ésimo número de Fibonacci recursivamente.
# Escribe una función recursiva que sume todos los números de una lista.
# Crea una función recursiva que invierta una cadena.
# Dada una lista anidada ([1, [2, [3, [4]]]]), crea una función recursiva que sume todos los elementos.
# Escribe una función recursiva que cuente cuántas veces aparece una letra en una cadena.
# Implementa una función recursiva que devuelva el máximo elemento de una lista.

# 🧱 6. Clases básicas
# Crea una clase Persona con nombre y edad; imprime una presentación usando un método.
# Crea una clase Rectangulo con ancho y alto, y un método que calcule su área.
# Crea una clase CuentaBancaria con depositar() y retirar(), y que mantenga el saldo.
# Crea una clase Libro con título, autor y año, y un método que devuelva su descripción.
# Crea una clase Punto con coordenadas x, y y un método para calcular la distancia entre dos puntos.
# Crea una clase Vehiculo con un método mover() y una subclase Coche que lo sobrescriba.
# Crea una clase Estudiante que reciba una lista de calificaciones y tenga un método para calcular el promedio.