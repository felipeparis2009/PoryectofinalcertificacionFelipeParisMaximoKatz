print("vamos a jugar al piedra papel tijera lagarto o goku")
from random import randint
elegi = ["piedra" , "papel" , "tijera" , "lagarto" , "goku"]
def main():
    bot = elegi[randint(0,4)]
    jugador = input("elgi alguna de estas opciones: ").lower()
    print ("bot elige alguna  de estas opciones: " + bot)
    if jugador == bot:
        print("empate")
    elif jugador == "piedra" and bot == "papel":
        print("el bot gano")
    elif jugador == "piedra" and bot == "tijera":
        print("ganaste")
    elif jugador == "piedra" and bot == "lagarto":
        print("ganaste")
    elif jugador == "piedra" and bot == "goku":
        print("el bot gano")
    elif jugador == "papel" and bot == "tijera":
        print("el bot gano")
    elif jugador == "papel" and bot == "piedra":
        print("ganaste")
    elif jugador == "papel" and bot == "lagarto":
        print("el bot gano")
    elif jugador == "papel" and bot == "goku":
        print("ganaste")
    elif jugador == "tijera" and bot == "piedra":
        print("el bot gano")
    elif jugador == "tijera" and bot == "papel":
        print("ganaste")
    elif jugador == "tijera" and bot == "lagarto":
        print("ganaste")
    elif jugador == "tijera" and bot == "goku":
        print("el bot gano")
    elif jugador == "lagarto" and bot == "piedra":
        print("el bot gano")
    elif jugador == "lagarto" and bot == "papel":
        print("ganaste")
    elif jugador == "lagarto" and bot == "tijera":
        print("el bot gano")
    elif jugador == "lagarto" and bot == "goku":
        print("ganaste")
    elif jugador == "goku" and bot == "piedra":
        print("ganaste")
    elif jugador == "goku" and bot == "papel":
        print("el bot gano")
    elif jugador == "goku" and bot == "tijera":
        print("ganaste")
    elif jugador == "goku" and bot == "lagarto":
        print("el bot gano")
    main()    

main()