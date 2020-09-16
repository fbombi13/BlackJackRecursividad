from random import Random


def valor_carta(carta):
    if carta == 'J' or carta == 'Q' or carta == 'K':
        return 10
    elif carta == 'A':
        return 0
    else:
        return int(carta)


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas_jugador = []


class Ventiuna:

    def __init__(self):
        self.cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.baraja = []
        self.generar_baraja()
        self.jugador = Jugador(input("Ingrese Nombre: "))
        self.maquina = Jugador("Maquina")

    def generar_baraja(self):
        i = 0
        while i < 4:
            self.baraja += self.cartas
            i += 1

    def sumar_cartas(self, cartas_jugador):
        cartas_jugador.count("A")
        if cartas_jugador.count("A") == 0:
            return self.sumar_cartas_enteras(cartas_jugador)
        else:
            if self.sumar_cartas_enteras(cartas_jugador) <= 10:
                return self.sumar_cartas_enteras(cartas_jugador) + 11 + (cartas_jugador.count("A") - 1)
            else:
                return self.sumar_cartas_enteras(cartas_jugador) + (cartas_jugador.count("A"))

    def sumar_cartas_enteras(self, cartas):
        if len(cartas) == 1:
            return valor_carta(cartas[0])
        else:
            return valor_carta(cartas[0]) + self.sumar_cartas_enteras(cartas[1:])

    def devuelve_carta(self):
        posicion = Random().randint(0, len(self.baraja) - 1)
        carta = self.baraja[posicion]
        self.baraja.remove(carta)
        return carta

    def iniciar(self):
        print("Bienvenido " + self.jugador.nombre)
        print("Sus primeras dos cartas son: ")
        self.jugador.cartas_jugador.append(self.devuelve_carta())
        self.jugador.cartas_jugador.append(self.devuelve_carta())
        print(self.jugador.cartas_jugador)
        print("\nCarta del Crupier: ")
        self.maquina.cartas_jugador.append(self.devuelve_carta())
        print(self.maquina.cartas_jugador)
        self.jugar(self.jugador, self.maquina)

    def jugar(self, jugador, maquina):
        if len(maquina.cartas_jugador) == 0 and len(jugador.cartas_jugador) == 0:
            self.iniciar()
        else:
            print("\n\n-----------Turno Jugador------------\n\n")
            self.crupier(True, jugador)

    def crupier(self, turno_jugador, jugador):
        if self.sumar_cartas(jugador.cartas_jugador) <= 21:

            if turno_jugador:
                if input("Oprima P para plantar u otra para pedir carta ").lower() != "p":
                    jugador.cartas_jugador.append(self.devuelve_carta())
                    print(jugador.cartas_jugador)
                    self.jugador.cartas_jugador = jugador.cartas_jugador
                    self.crupier(True, jugador)
                else:
                    print("\n\n-----------Turno Maquina------------\n\n")
                    self.crupier(False, self.maquina)
            else:
                jugador.cartas_jugador.append(self.devuelve_carta())
                print(jugador.cartas_jugador)
                if self.sumar_cartas(self.jugador.cartas_jugador) <= self.sumar_cartas(jugador.cartas_jugador) <= 21:
                    print("Ganó " + self.maquina.nombre)
                    return
                else:
                    print("Ganando " + self.jugador.nombre)
                self.crupier(False, jugador)
        else:
            print("\n\n\n------------------------------------\n Perdió   " + jugador.nombre)


####### JUGAR
ventiuna = Ventiuna()
ventiuna.jugar(ventiuna.jugador, ventiuna.maquina)
