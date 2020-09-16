from random import Random


def valor_carta(carta):
    if carta == 'J' or carta == 'Q' or carta == 'K':
        return 10
    elif carta == 'A':
        return 0
    else:
        return int(carta)


def devuelve_carta(cartas):
    return cartas[Random().randint(0, len(cartas) - 1)]


def generar_baraja(cartas):
    if len(cartas) < 52:
        return generar_baraja(cartas + cartas)
    else:
        return cartas


def sumar_cartas(cartas_jugador):
    cartas_jugador.count("A")
    if cartas_jugador.count("A") == 0:
        return sumar_cartas_enteras(cartas_jugador)
    else:
        if sumar_cartas_enteras(cartas_jugador) <= 10:
            return sumar_cartas_enteras(cartas_jugador) + 11 + (cartas_jugador.count("A") - 1)
        else:
            return sumar_cartas_enteras(cartas_jugador) + (cartas_jugador.count("A"))


def sumar_cartas_enteras(cartas):
    if len(cartas) == 1:
        return valor_carta(cartas[0])
    else:
        return valor_carta(cartas[0]) + sumar_cartas_enteras(cartas[1:])


def iniciar(jugador, maquina, cartas):
    print("Sus primeras dos cartas son: ")
    jugador.append(devuelve_carta(cartas))
    cartas.remove(jugador[-1])
    jugador.append(devuelve_carta(cartas))
    cartas.remove(jugador[-1])
    print(jugador)
    print("\nCarta del Crupier: ")
    maquina.append(devuelve_carta(cartas))
    cartas.remove(maquina[-1])
    print(maquina)
    jugar(jugador, maquina, cartas)


def jugar(jugador, maquina, cartas):
    if len(maquina) == 0 and len(jugador) == 0:
        iniciar(jugador, maquina, cartas)
    else:
        crupier(True, jugador, maquina, cartas)


def crupier(turno_jugador, jugador, maquina, cartas):
    if turno_jugador:
        print("\n\n-----------Turno Jugador------------\n\n")
        if sumar_cartas(jugador) <= 21:
            if input("Oprima P para plantar u otra para pedir carta ").lower() != "p":
                jugador.append(devuelve_carta(cartas))
                cartas.remove(jugador[-1])
                print(jugador)
                crupier(True, jugador, maquina, cartas)
            else:
                print("\n\n-----------Turno Maquina------------\n\n")
                crupier(False, jugador, maquina, cartas)
        else:
            print("\n\n\n------------------------------------\n Perdió  Jugador")
    else:
        maquina.append(devuelve_carta(cartas))
        cartas.remove(maquina[-1])
        print(maquina)
        if sumar_cartas(jugador) <= sumar_cartas(maquina) <= 21:
            print("Ganó la Maquina")
        elif sumar_cartas(maquina) <= 21:
            print("Ganando Jugador")
            crupier(False, jugador, maquina, cartas)
        else:
            print("Ganó Jugador")


while input("\n\n Presione X para jugar y Q para salir ").lower() != "q":
    jugar([], [], generar_baraja(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]))
