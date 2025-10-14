# LISTS

# 1 Delete duplicates keeping the order
def delete_duplicates(arr):
    # order dict
    order_dict = dict.fromkeys(arr)
    
    # Return onlye dict keys
    return list(order_dict.keys())
    
numbs = [4, 5, 2, 4, 8, 2, 9, 10, 8]
print(delete_duplicates(numbs))

# 2 Invert words in a sentence

def invert_sentence(phrase):
    return [ word for word in phrase.split()][::-1]

sentence = "Aprender Python es divertido"

print(invert_sentence(sentence))

# 3️ Sumar solo los impares mayores que 5
def sum_odd_higher_five(arr):
    total = 0
    
    for x in arr:
        if x > 5:
            if x % 2 != 0:
                total += x
            
    return total

numeros = [3, 7, 8, 9, 2, 11, 13, 4]
print(sum_odd_higher_five(numeros))

# 4️ (List comprehension) Crear lista de cuadrados de números pares

def square_values(arr):
    return [n ** 2 for n in arr if n % 2 == 0]

values = [1, 2, 3, 4, 5, 6]
print(square_values(values))

# SETS
a = {"rojo", "azul", "verde"}
b = {"verde", "amarillo", "azul"}

# Elementos comunes (intersección)
comunes = a & b
print("Comunes:", comunes)  # {'azul', 'verde'}

# Solo en A (diferencia)
solo_a = a - b
print("Solo en A:", solo_a)  # {'rojo'}

# Unión de ambos sets
union = a | b
print("Unión:", union)  # {'rojo', 'azul', 'verde', 'amarillo'}

lenguajes = {"Python", "Java", "C++", "JavaScript"}
favoritos = {"Python", "Java"}

# ¿favoritos está dentro de lenguajes?
print(favoritos.issubset(lenguajes))  # True

# ¿lenguajes contiene a favoritos?
print(lenguajes.issuperset(favoritos))  # True

frase = "python es genial y python es poderoso"

# Convertir a set y eliminar duplicados
palabras = set(frase.split())

# Para eliminar "python" y "es" que se repiten
palabras_unicas = {p for p in palabras if frase.split().count(p) == 1}
print(palabras_unicas)  # {'genial', 'y', 'poderoso'}

# 4️ (Set comprehension) Crear conjunto de números pares al cuadrado
def square_set(arr):
    return { n ** 2 for n in arr if n % 2 == 0}

v = [1, 2, 3, 4, 5, 6]
print(square_set(v))


palabra = "programacion"
vocales_unicas = {letra for letra in palabra if letra in "aeiou"}
print(vocales_unicas)  # {'o', 'a', 'i'}

texto = "python es poderoso y python es divertido"
palabras = texto.split()
frecuencia = {palabra: palabras.count(palabra) for palabra in set(palabras)}
print(frecuencia)
# {'python': 2, 'es': 2, 'poderoso': 1, 'y': 1, 'divertido': 1}

paises = {"mx": "México", "us": "Estados Unidos", "ca": "Canadá"}
invertido = {valor: clave for clave, valor in paises.items()}
print(invertido)
# {"México": "mx", "Estados Unidos": "us", "Canadá": "ca"}

ventas_a = {"manzanas": 10, "peras": 5, "uvas": 3}
ventas_b = {"peras": 4, "uvas": 7, "naranjas": 8}

fusionadas = {k: ventas_a.get(k, 0) + ventas_b.get(k, 0) for k in set(ventas_a) | set(ventas_b)}
print(fusionadas)
# {'manzanas': 10, 'peras': 9, 'uvas': 10, 'naranjas': 8}

cubos = {n: n**3 for n in range(1, 6)}
print(cubos)
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10

punto = (3, 4)
x, y = punto
print(x, y)  # 3 4

pares = [("nombre", "Gus"), ("edad", 28), ("lenguaje", "Python")]
dic = dict(pares)
print(dic)
# {'nombre': 'Gus', 'edad': 28, 'lenguaje': 'Python'}

numeros = [1, 2, 3, 4, 5]
cuadrados = tuple(n**2 for n in numeros)
print(cuadrados)
# (1, 4, 9, 16, 25)