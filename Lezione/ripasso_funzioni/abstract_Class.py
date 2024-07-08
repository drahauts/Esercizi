from abc import ABC, abstractmethod

class AbcAnimal(ABC):


    @abstractmethod
    def verso():
        
        pass

    @abstractmethod
    def movimento(self, t: int):
        
        pass

class Cane(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()


        self.nome = nome
        self.velocita: float = 10.0 #m/s


    def verso(self):
        return "Bau!"
    
    def movimento(self, t: int):
        return self.velocita * t

class Gatto(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome = nome
    def verso(self):
        return "Meow!"
    
    def movimento(self, t: int):
        return 10.0 * t

cane_1: Cane = Cane(nome= "Pluto")
cane_1.verso()
cane_1.movimento(10)

gatto_1: Gatto = Gatto(nome= "Lucy")
gatto_1.verso()
gatto_1.movimento(10)