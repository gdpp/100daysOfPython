print("""
               *         .              *            _.---._      
                             ___   .            ___.'       '.   *
        .              _____[LLL]______________[LLL]_____     *
                      /     [LLL]              [LLL]     \     |
                     /____________________________________\    |    .
                      )==================================(    /
     .      *         '|I .-. I .-. I .--. I .-. I .-. I|'  .'
                  *    |I |+| I |+| I |. | I |+| I |+| I|-'`       *
                       |I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I|      .
              .       |_I_____I_____I______I_____I_____I_|
                       )================================(   *
       *         _     |I .-. I .-. I .--. I .-. I .-. I|          *
                |u|  __|I |+| I |+| I |<>| I |+| I |+| I|    _         .
           __   |u|_|uu|I |+| I |+| I |~ | I |+| I |+| I| _ |U|     _
       .  |uu|__|u|u|u,|I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I||n|| |____|u|
          |uu|uu|_,.-' /I_____I_____I______I_____I_____I\`'-. |uu u|u|__
          |uu.-'`      #############(______)#############    `'-. u|u|uu|
         _.'`              ~"^"~   (________)   ~"^"^~           `'-.|uu|
      ,''          .'    _                             _ `'-.        `'-.
  ~"^"~    _,'~"^"~    _( )_                         _( )_   `'-.        ~"^"~
      _  .'            |___|                         |___|      ~"^"~     _
    _( )_              |_|_|          () ()          |_|_|              _( )_
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/[===]\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
~""~|_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_lc|~""~
   [_____]            [_____]                       [_____]            [_____]
""")
print('''
In the sleepy village of Elderwood, Eliza steps into the long-abandoned Hollow Inn to unravel her uncle's mysterious disappearance. Inside, she discovers not just family secrets, but echoes of a forgotten love. Join her in "Echoes of the Hollow Inn," where every shadow and whisper holds a piece of the puzzle.
''')

print("The Front Door is slightly ajar, vines creeping over its frame. Do you:")

print("A. Push the door open and enter.")
print("B. Look for another way in.")

opc = input("Choose A or B: ")

if opc == "A":
    print("You push the door open, which creaks ominously. Dust motes dance in the beam of your flashlight as you step inside. The air is musty and cold.")

    print("You're now in a grand foyer with a grand staircase and two doors, one on each side. Do you:")

    print("A. Take the staircase up.")
    print("B. Go through the left door.")
    print("C. Go through the right door.")

    opc = input("Choose A, B, or C:")

    if opc == "A":
        print("You ascend the creaking staircase to find a long hallway with several doors.")

        print("Do you enter the first or second door?")

        opc = input("Choose first or second")

        if opc == 'first':
            print("Leads to a peaceful library and a clue about the house's history")
        else:
            print("A ghostly presence overwhelms you, forcing you out of the house in terror.")
            print("Game Over!")
    elif opc == "B":
        print("You find yourself in a dusty library full of old books. Do you:")
        
        print("A. Browse the books.")
        print("B. Look for a secret passage.")

        opc  = input("Choose A or B")

        if opc == "A":
            print("You finds a hidden diary revealing the mansion's past")
            print("End of the game!")

        else:
            print("You fall into a trap!")
            print("Game OVer!")
    else:
        print("you stumble into a collapsing room and are forced to flee the house")
        print("Game Over!")
else:
    print("You wander around the house and eventually decide to leave, too spooked to continue.")
    print("Game Over!")