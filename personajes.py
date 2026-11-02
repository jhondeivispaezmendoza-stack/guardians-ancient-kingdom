from abc import ABC, abstractmethod
from math import floor
class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if vida <= 0:
            raise ValueError("La vida debe ser mayor que cero.")
        if ataque < 0 or defensa < 0:
            raise ValueError("El ataque y la defensa no pueden ser negativos.")
        self.nombre = nombre
        self._vida = vida
        self.ataque = ataque
        self.defensa = defensa
    @property
    def vida(self):
        return self._vida
    @property
    def esta_vivo(self):
        return self._vida > 0
    def recibir_danio(self, cantidad):
        if cantidad < 0:
            raise ValueError("El daño no puede ser negativo.")
        self._vida = max(0, self._vida - cantidad)
    @abstractmethod
    def atacar(self, objetivo):
        pass
class Guerrero(Personaje):
    def atacar(self, objetivo):
        danio = max(0, floor(self.ataque * 1.20 - objetivo.defensa))
        objetivo.recibir_danio(danio)
        return danio
class Mago(Personaje):
    def atacar(self, objetivo):
        danio = self.ataque
        objetivo.recibir_danio(danio)
        return danio
class Arquero(Personaje):
    def atacar(self, objetivo):
        if self.ataque > objetivo.defensa:
            danio = 2 * (self.ataque - objetivo.defensa)
        else:
            danio = 0
        objetivo.recibir_danio(danio)
        return danio
class Combate:
    def __init__(self, personaje1, personaje2, limite_rondas=50):
        self.personaje1 = personaje1
        self.personaje2 = personaje2
        self.limite_rondas = limite_rondas
        self.historial = []
    def iniciar(self):
        ronda = 0
        while (
            self.personaje1.esta_vivo
            and self.personaje2.esta_vivo
            and ronda < self.limite_rondas
        ):
            ronda += 1
            vida1_antes = self.personaje1.vida
            vida2_antes = self.personaje2.vida
            danio1 = self.personaje1.atacar(self.personaje2)
            if self.personaje2.esta_vivo:
                danio2 = self.personaje2.atacar(self.personaje1)
            else:
                danio2 = 0
            resultado = (
                f"Ronda {ronda}: "
                f"{self.personaje1.nombre} causa {danio1} de daño; "
                f"{self.personaje2.nombre} causa {danio2} de daño."
            )
            self.historial.append(resultado)
            if (
                vida1_antes == self.personaje1.vida
                and vida2_antes == self.personaje2.vida
            ):
                self.historial.append(
                    "Combate terminado en empate: nadie causó daño."
                )
                return "Empate"
        if self.personaje1.esta_vivo and not self.personaje2.esta_vivo:
            ganador = self.personaje1.nombre
        elif self.personaje2.esta_vivo and not self.personaje1.esta_vivo:
            ganador = self.personaje2.nombre
        else:
            ganador = "Empate"
        self.historial.append(f"Resultado final: {ganador}")
        return ganador
