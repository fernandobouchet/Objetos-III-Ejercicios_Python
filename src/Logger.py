class Logger:
    class NivelesLogger:
        INFO = "INFO"
        WARN = "WARN"
        ERROR = "ERROR"

    def __init__(self, nivel_logger):
        if nivel_logger.upper() == self.NivelesLogger.INFO:
            self.logger_actual = self.NivelesLogger.INFO
        elif nivel_logger.upper() == self.NivelesLogger.WARN:
            self.logger_actual = self.NivelesLogger.WARN
        elif nivel_logger.upper() == self.NivelesLogger.ERROR:
            self.logger_actual = self.NivelesLogger.ERROR
        else:
            raise ValueError("No es posible asignar el nivel de logger indicado")

    def show_info(self, message):
        if self.logger_actual != self.NivelesLogger.INFO:
            return
        print(f"INFO: {message}")

    def show_warn(self, message):
        if self.logger_actual == self.NivelesLogger.ERROR:
            return
        print(f"WARN: {message}")

    def show_error(self, message):
        print(f"ERROR: {message}")
