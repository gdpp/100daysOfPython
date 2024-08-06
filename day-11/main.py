"""
Blackjack Project
Understand the Rules of the Game

    -   The objective is to score 21 points or get as close as possible without going over.
    -   Players compete against the dealer, not each other.
    -   Cards 2 to 10 are worth their face value
    -   Face cards (J, Q, K) are worth 10 points
    -   The Ace can be worth 1 or 11 points.
    -   Each player initially receives two cards, and can hit (get more) or stand.

Game Design
Defines the main components of the game

    -   Cards and Deck: Create a standard deck of 52 cards.
    -   Players: Include at least one player and the dealer.
    -   Game Mechanics: Handle the actions of hit, stand and determine the winner.  
"""

def main():
    pass


#init game
main()


# Implementa la lógica para inicializar una nueva partida:

#     Crear y Mezclar la Baraja: Crea una lista que represente una baraja de cartas y mézclala aleatoriamente.
#     Repartir Cartas: Reparte dos cartas a cada jugador y al crupier.

# Paso 4: Implementar las Funciones Principales

# Divide el juego en funciones específicas:



#     Calcular Valor de la Mano: Una función para calcular el valor de la mano de un jugador o del crupier.
#     Mostrar Cartas: Una función para mostrar las cartas de un jugador y la carta visible del crupier.

# Paso 5: Implementar el Turno del Jugador

# Permitir que el jugador tome decisiones:

#     Pedir Cartas (Hit): Añadir una carta a la mano del jugador y verificar si ha excedido 21 puntos.
#     Plantarse (Stand): Finalizar el turno del jugador.

# Paso 6: Implementar el Turno del Crupier

# Definir las reglas para el crupier:

#     Reglas del Crupier: El crupier debe pedir cartas hasta alcanzar al menos 17 puntos.
#     Mostrar Cartas del Crupier: Una vez que el crupier termina su turno, mostrar todas sus cartas.

# Paso 7: Determinar el Ganador

# Desarrollar la lógica para determinar el resultado del juego:

#     Comparar Manos: Comparar los valores de las manos del jugador y del crupier.
#     Determinar Resultado: Decidir el ganador basado en quién tiene el valor más alto sin pasarse de 21.


# Estructura Sugerida del Código

# Divide tu código en secciones para mantenerlo organizado:

#     Sección de Inicialización: Crear la baraja y mezclarla.
#     Sección de Reparto: Repartir cartas a los jugadores y al crupier.
#     Sección de Juego: Implementar la lógica del turno del jugador y del crupier.
#     Sección de Resultado: Determinar y mostrar el ganador.