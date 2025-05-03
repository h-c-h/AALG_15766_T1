import random

class Equipo:
    def __init__(self, nombre = "", partidosGanados = 0, partidosPerdidos = 0, setGanados = 0):
        self.nombre = nombre
        self.partidosGanados = partidosGanados
        self.partidosPerdidos = partidosPerdidos
        self.setGanados = setGanados

    def __str__(self):
        return f"Equipo: {self.nombre}, Ganados: {self.partidosGanados}, Perdidos: {self.partidosPerdidos}, Sets ganados actuales: {self.setGanados}"

def RegistraSet(equipo1, equipo2, ganador_num):
    if ganador_num == 1:
        equipo1.setGanados += 1
        if equipo1.setGanados == 3:
            equipo1.partidosGanados += 1
            equipo2.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0
    elif ganador_num == 2:
        equipo2.setGanados += 1
        if equipo2.setGanados == 3:
            equipo2.partidosGanados += 1
            equipo1.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido(equipo1, equipo2):
    sets_equipo1 = 0
    sets_equipo2 = 0
    set_num = 1

    while sets_equipo1 < 3 and sets_equipo2 < 3:
        puntos1 = Puntos()
        puntos2 = Puntos()

        if puntos1 >= 25 or puntos2 >= 25:
            if puntos1 >= 25 and puntos1 >= puntos2:
                RegistraSet(equipo1, equipo2, 1)
                sets_equipo1 += 1
                print(f"Set {set_num}: {equipo1.nombre} {puntos1} - {equipo2.nombre} {puntos2}. Gana {equipo1.nombre}")
            elif puntos2 >= 25 and puntos2 > puntos1:
                RegistraSet(equipo1, equipo2, 2)
                sets_equipo2 += 1
                print(f"Set {set_num}: {equipo1.nombre} {puntos1} - {equipo2.nombre} {puntos2}. Gana {equipo2.nombre}")
        else:
            while True:
                puntos1 += PuntosExtras()
                puntos2 += PuntosExtras()
                if puntos1 >= 25 or puntos2 >= 25:
                    if puntos1 > puntos2:
                        RegistraSet(equipo1, equipo2, 1)
                        sets_equipo1 += 1
                        print(f"Set {set_num}: {equipo1.nombre} {puntos1} - {equipo2.nombre} {puntos2}. Gana {equipo1.nombre} (con extras)")
                    elif puntos2 > puntos1:
                        RegistraSet(equipo1, equipo2, 2)
                        sets_equipo2 += 1
                        print(f"Set {set_num}: {equipo1.nombre} {puntos1} - {equipo2.nombre} {puntos2}. Gana {equipo2.nombre} (con extras)")
                    break

        set_num += 1

    print(f"Ganador del partido: {equipo1.nombre if sets_equipo1 > sets_equipo2 else equipo2.nombre} ({sets_equipo1}-{sets_equipo2})")
    print("----- Nuevo partido -----\n")

def ResultadoTorneo(equipo1, equipo2):
    print("Resultados finales:")
    print(f"{equipo1.nombre} - Partidos Ganados: {equipo1.partidosGanados}, Partidos Perdidos: {equipo1.partidosPerdidos}")
    print(f"{equipo2.nombre} - Partidos Ganados: {equipo2.partidosGanados}, Partidos Perdidos: {equipo2.partidosPerdidos}")

if __name__ == "__main__":
    nombre1 = input("Nombre del Equipo 1: ")
    nombre2 = input("Nombre del Equipo 2: ")

    equipo1 = Equipo(nombre1)
    equipo2 = Equipo(nombre2)

    partidos_a_jugar = int(input("¿Cuántos partidos deben jugar ambos equipos? "))

    for _ in range(partidos_a_jugar):
        JugarPartido(equipo1, equipo2)

    ResultadoTorneo(equipo1, equipo2)