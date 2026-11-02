from personajes import Guerrero, Mago, Arquero, Combate


def mostrar_personaje(personaje):
    print(
        f"{personaje.nombre} | "
        f"Vida: {personaje.vida} | "
        f"Ataque: {personaje.ataque} | "
        f"Defensa: {personaje.defensa}"
    )


def main():
    print("=" * 50)
    print("GUARDIANS OF THE ANCIENT KINGDOM")
    print("Sistema de combate por turnos")
    print("=" * 50)

    guerrero = Guerrero("Aldric", 120, 25, 12)
    mago = Mago("Elyra", 90, 30, 5)
    arquero = Arquero("Kael", 100, 22, 8)

    personajes = [guerrero, mago, arquero]

    print("\nPERSONAJES DISPONIBLES")
    for personaje in personajes:
        mostrar_personaje(personaje)

    print("\nCOMBATE: ALDRIC VS ELYRA")
    combate = Combate(guerrero, mago)
    ganador = combate.iniciar()

    for evento in combate.historial:
        print(evento)

    print(f"\nResultado del combate: {ganador}")

    print("\nESTADO FINAL DE LOS PERSONAJES")
    for personaje in personajes:
        mostrar_personaje(personaje)

    print("\nFin del programa.")


if __name__ == "__main__":
    main()
