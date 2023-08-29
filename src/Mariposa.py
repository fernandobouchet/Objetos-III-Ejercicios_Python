from ComerYVolar import ComerYVolar
from Logger import Logger


class Mariposa(ComerYVolar):

    def __init__(self, nombre, peso, log: Logger):
        self.nombre = nombre
        self.__peso = peso
        self.__kmsRecorridos = 0
        self.log = log

    def comer(self, gramos):
        self.__peso += gramos / 5
        self.log.show_info(f"La mariposa {self.nombre} comió {gramos}, su peso aumentó a {self.__peso}")

    def volar(self, kilometros):
        self.__kmsRecorridos += kilometros
        self.log.show_info(f"La mariposa {self.nombre} recorrió {kilometros} kilometros, sus kilometros recorridos "
                          f"aumentó a {self.__kmsRecorridos}")

    def obtener_kms_recorridos(self):
        self.log.show_info(f"La kilometros recorridos de {self.nombre} son {self.__kmsRecorridos}")
        return self.__kmsRecorridos
