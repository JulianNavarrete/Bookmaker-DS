from datetime import datetime
from colorama import init, Fore


init(autoreset=True)


class LoggerConsole:

    def info(self, mensaje, valor):
        print(datetime.now(), Fore.BLUE+" INFO: ", mensaje, valor)

    def warning(self, mensaje, valor):
        print(datetime.now(), Fore.YELLOW+" WARN: ", mensaje, valor)

    def error(self, mensaje, valor):
        print(datetime.now(), Fore.RED+" ERR: ", mensaje, valor)

    def debug(self, mensaje, valor):
        print(datetime.now(), Fore.GREEN+" DEB: ", mensaje, valor)


class LoggerFile:

    def info(self, mensaje, valor):
        with open("file_log.txt", "a") as file:
            log_out = (str(datetime.now()), " INFO: ", mensaje + " " + str(valor), "\n")
            file.writelines(log_out)

    def warning(self, mensaje, valor):
        with open("file_log.txt", "a") as file:
            log_out = (str(datetime.now()), " WARN: ", mensaje + " " + str(valor), "\n")
            file.writelines(log_out)

    def error(self, mensaje, valor):
        with open("file_log.txt", "a") as file:
            log_out = (str(datetime.now()), " ERR: ", mensaje + " " + str(valor), "\n")
            file.writelines(log_out)

    def debug(self, mensaje, valor):
        with open("file_log.txt", "a") as file:
            log_out = (str(datetime.now()), " DEB: ", mensaje + " " + str(valor), "\n")
            file.writelines(log_out)


if __name__ == "__main__":

    type_log = input("Ingrese la letra " + '"' + "c" + '"' + " para salida por consola o la letra "+ '"' + "f" + '"' + " para salida por archivo log: ")
    if type_log == "c":
        log = LoggerConsole()
    elif type_log == "f":
        log = LoggerFile()
    else:
        exit(1)
    log.info("Valor de variable", 1234)
    log.warning("Valor de warning", 2345)
    log.error("Valor de error", 7896)
    log.debug("Valor de debug", 9999)
