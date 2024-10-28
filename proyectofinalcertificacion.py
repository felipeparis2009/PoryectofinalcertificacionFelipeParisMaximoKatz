print("vamos a jugar al piedra papel o tijera")
from random import randint
elegi = ["piedra" , "papel" , "tijera"]
def main():
    bot = elegi[randint(0,2)]
    jugador = input("elgi alguna de estas opciones: ").lower()
    print ("bot elige alguna estas opciones: " + bot)
    if jugador == bot:
        print("empate")
    elif jugador == "piedra" and bot == "papel":
        print("el bot gano")
    elif jugador == "piedra" and bot == "tijera":
        print("ganaste")
    elif jugador == "papel" and bot == "tijera":
        print("el bot gano")
    elif jugador == "papel" and bot == "piedra":
        print("ganaste")
    elif jugador == "tijera" and bot == "piedra":
        print("el bot gano")
    elif jugador == "tijera" and bot == "papel":
        print("ganaste")
    main()
main()