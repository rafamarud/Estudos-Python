class Termostato:
    
    def __init__(self, temperatura = 24):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__Temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f"Temperatura de {valor} é inválida!")
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}{chr(176)}C"