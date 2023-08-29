import logging
from ComerYVolar import ComerYVolar
from Logger import Logger


class Ave(ComerYVolar):
    def __init__(self, nombre, log:Logger):
        self.__energia = 2
        self.__kms_recorridos = 0
        self.nombre = nombre
        self.log = log

    def comer(self, gramos):
        self.__energia += gramos
        self.log.show_info(f"{self.nombre} comió {gramos} gramos, su energía aumentó a {self.__energia}")

    def puede_volar(self, kilometros):
        return kilometros * 3 < self.__energia

    def volar(self, kilometros):
        if self.__energia <= 0 or not self.puede_volar(kilometros):
            self.log.show_error(f"{self.nombre} no tiene suficiente energía para volar {kilometros} kilometros")
            raise Exception("La energía no es suficiente para volar.")

        self.__energia -= kilometros * 3
        self.__kms_recorridos += kilometros
        self.log.show_info(f"{self.nombre} voló {kilometros} kilometros, su energía disminuyó a {self.__energia}")

    def obtener_energia(self):
        self.log.show_info(f"El nivel de energía de {self.nombre} es {self.__energia}")
        return self.__energia

    def obtener_kms_recorridos(self):
        self.log.show_info(f"Los kilometros recorridos de {self.nombre} son {self.__kms_recorridos}")
        return self.__kms_recorridos
