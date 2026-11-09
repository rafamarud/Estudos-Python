from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    
    def preparar(self):
        print(" -- Iniciando o preparo -- ")
        print(self.ferver_agua())
        print(self.misturar())
        print(self.servir())
        print(" -- Bebida pronta -- ")

    def ferver_agua(self):
        return f"1) Fervendo água..."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass