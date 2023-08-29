from abc import ABC, abstractmethod


class ComerYVolar(ABC):
    @abstractmethod
    def comer(self, gramos):
        pass

    @abstractmethod
    def volar(self, kilometros):
        pass

    @abstractmethod
    def obtener_kms_recorridos(self):
        pass
