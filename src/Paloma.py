from Aves import Ave


class Paloma(Ave):
    def __init__(self, nombre, log):
        super().__init__(nombre, log)

    def ir_al_banio(self):
        self.__energia -= 1
        self.__kms_recorridos += 1
        self.log.show_info(f"La paloma {self.nombre} fué al baño, su energia disminuyó a {self.__energia} y sus "
                          f"kilometros recorridos aumentaron a{self.__kms_recorridos}")
