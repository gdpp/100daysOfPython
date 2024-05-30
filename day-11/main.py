# Paso 1: Entender las Reglas del Juego

# Asegúrate de entender completamente las reglas del Black Jack:

#     El objetivo es sumar 21 puntos o acercarse lo más posible sin pasarse.
#     Los jugadores compiten contra el crupier (dealer), no entre ellos.
#     Las cartas del 2 al 10 valen su valor nominal, las figuras (J, Q, K) valen 10 puntos y el As puede valer 1 u 11 puntos.
#     Cada jugador recibe inicialmente dos cartas, y puede pedir más (hit) o plantarse (stand).

# Paso 2: Diseño del Juego

# Define los componentes principales del juego:

#     Cartas y Baraja: Crear una baraja estándar de 52 cartas.
#     Jugadores: Incluir al menos un jugador y el crupier.
#     Mecánica del Juego: Manejar las acciones de hit, stand y determinar el ganador.

# Paso 3: Inicializar el Juego

# Implementa la lógica para inicializar una nueva partida:

#     Crear y Mezclar la Baraja: Crea una lista que represente una baraja de cartas y mézclala aleatoriamente.
#     Repartir Cartas: Reparte dos cartas a cada jugador y al crupier.

# Paso 4: Implementar las Funciones Principales

# Divide el juego en funciones específicas:

#     Crear Baraja: Una función para crear y devolver una baraja de cartas.
#     Mezclar Baraja: Una función para mezclar la baraja.
#     Repartir Cartas: Una función para repartir cartas a un jugador o al crupier.
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

# Paso 8: Añadir Funcionalidades Adicionales

# Mejora el juego con características opcionales:

#     Apuestas: Permitir que los jugadores hagan apuestas al inicio de la partida.
#     Multiples Jugadores: Adaptar las funciones para manejar varios jugadores en una partida.
#     División de Cartas (Split): Permitir que el jugador divida la mano si las dos primeras cartas son iguales.

# Paso 9: Manejar Errores y Validaciones

# Asegúrate de que tu juego maneje errores y casos especiales:

#     Validar Entradas: Asegurarse de que las entradas del usuario son válidas (por ejemplo, solo aceptar 'hit' o 'stand').
#     Manejo de Excepciones: Manejar posibles errores, como intentar repartir cartas de una baraja vacía.

# Paso 10: Prueba y Depuración

# Prueba tu juego exhaustivamente:

#     Prueba de Funcionalidades: Verifica cada función individualmente.
#     Prueba del Flujo del Juego: Asegúrate de que el flujo del juego es claro y libre de errores.

# Paso 11: Documentación y Comentarios

# Documenta tu código y proporciona instrucciones claras:

#     Comentarios en el Código: Añade comentarios útiles en tu código para explicar la lógica.
#     README: Escribe un archivo README con instrucciones sobre cómo jugar y cualquier requerimiento adicional.

# Estructura Sugerida del Código

# Divide tu código en secciones para mantenerlo organizado:

#     Sección de Inicialización: Crear la baraja y mezclarla.
#     Sección de Reparto: Repartir cartas a los jugadores y al crupier.
#     Sección de Juego: Implementar la lógica del turno del jugador y del crupier.
#     Sección de Resultado: Determinar y mostrar el ganador.

# Siguiendo estos pasos detallados, deberías poder crear un juego de Black Jack en la consola utilizando Python sin programación orientada a objetos. ¡Buena suerte con tu proyecto capstone!