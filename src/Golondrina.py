import random
from Aves import Ave


class Golondrina(Ave):
    def __init__(self, nombre, log):
        super().__init__(nombre, log)
        self.__es_mejor_pescador = False
        self.__ya_pesco = False
        self.__intentos_de_pesca = 0

    def hacer_mejor_pescador(self):
        self.__es_mejor_pescador = True
        self.log.show_info(f"La golondrina {self.nombre} es ahora mejor pescador")

    def puede_pescar(self):
        if self.__es_mejor_pescador:
            return self.__energia >= 2
        else:
            return self.__energia >= 3

    def pescar(self):
        self.log.show_info(f"La golondrina {self.nombre} intenta pescar.")

        if not self.puede_pescar():
            self.log.show_error(f"La energía de {self.nombre} no es suficiente para poder pescar.")
            raise Exception("La energía no es suficiente para poder pescar.")

        if self.__es_mejor_pescador:
            self.__energia -= 1
            self.log.show_info(f"{self.nombre} es mejor pescador, se le descuenta 1 de energía.")
        else:
            self.log.show_info(f"{self.nombre} no es mejor pescador, se le descuenta 2 de energía.")
            self.__energia -= 2

        self.__intentos_de_pesca += 1
        self.__kms_recorridos += 1
        self.log.show_info(f"{self.nombre} suma 1 intento de pesca y 1 kilómetro recorrido.")

        if not self.__ya_pesco and self.__intentos_de_pesca < 10:
            self.__ya_pesco = random.choice([True, False])
            self.log.show_info(f"Intento de pesca de {self.nombre} número: {self.__intentos_de_pesca}")

            if self.__ya_pesco:
                self.__energia += 10
                self.log.show_info(f"{self.nombre} pescó!, su energía asciende a {self.__energia}")
            else:
                self.log.show_info(f"{self.nombre} no tuvo éxito al pescar esta vez.")
        elif self.__ya_pesco and self.__intentos_de_pesca <= 10:
            if self.__intentos_de_pesca == 10:
                self.__intentos_de_pesca = 0
                self.log.show_info(f"{self.nombre} ya pesco, y sus intentos de pesca son 10, se resetean los intentos")
            else:
                self.log.show_info(f"{self.nombre} ya pesco, este es el intento número {self.__intentos_de_pesca}")
        else:
            self.__ya_pesco = True
            self.__energia += 10
            self.log.show_info(f"{self.nombre} pescó en el último intento, su energía asciende a {self.__energia}")
