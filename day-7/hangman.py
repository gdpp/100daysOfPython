import random

def leer_palabras(archivo):
    with open(archivo, 'r') as file:
        palabras = file.readlines()
    # Eliminar saltos de línea y espacios en blanco
    palabras = [palabra.strip() for palabra in palabras]
    return palabras

def seleccionar_palabra(palabras):
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    return ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

def ahorcado():
    palabras = leer_palabras('hangman_words.txt')
    palabra_secreta = seleccionar_palabra(palabras)
    letras_adivinadas = set()
    intentos = 6
    errores = 0

    print("¡Bienvenido al juego del ahorcado!")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas))

    while errores < intentos:
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
        elif letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            letras_adivinadas.add(letra)
            errores += 1
            print(f"Letra incorrecta. Te quedan {intentos - errores} intentos.")

        progreso = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso)

        if '_' not in progreso:
            print("¡Felicidades! Has adivinado la palabra.")
            break
    else:
        print(f"Lo siento, has perdido. La palabra era '{palabra_secreta}'.")

if __name__ == "__main__":
    ahorcado()