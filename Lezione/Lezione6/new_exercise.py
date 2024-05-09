class Person:
    def __init__(self,
                 name: str,
                 cognome: str,
                 data_di_nascita: str,
                 genere: str) -> None:
        
        self.name: str = name
        self.cognome: str = cognome
        self.data_di_nascita: str = data_di_nascita
        self.genere: str = genere


    def calcola_età(self) -> int:
        return 10
    
    def __str__(self) -> str:
        return f"Person(nome: {self.name}, cognome: {self.cognome}, data_di_nascita: {self.data_di_nascita}, genere: {self.genere})"


persona1: Person = Person(name= "Paolo",
                          cognome= "Armandi",
                          data_di_nascita= "21/04/1989",
                          genere= "M")

class Dipendente(Person):
    def __init__(self,
                 name: str,
                 cognome: str,
                 data_di_nascita: str,
                 genere: str,
                 ore_lavorate: int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere)
        self.ore_lavorate = ore_lavorate

    def calcola_stipendio(self) -> float:
        return 600.0
    
    def __str__(self) -> str:
        return super().__str__()

dipendente1: Dipendente = Dipendente(name= "Paolo",
                                     cognome= "Armandi",
                                     data_di_nascita= "21/04/1989",
                                     genere= "M",
                                     ore_lavorate= 500)

class Professore(Dipendente):
    def __init__(self,
                 name: str,
                 cognome: str,
                 data_di_nascita: str,
                 genere: str,
                 ore_lavorate: int,
                 maretia_insegnata: str,
                 ore_di_lezione: int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere, ore_lavorate)

        self.materia_insegnata = maretia_insegnata
        self.ore_di_lezione = ore_di_lezione

    
    def __str__(self) -> str:
        return f"Professor {self.name}, {self.cognome}"


professore1: Professore= Professore(name= "Paolo",
                                     cognome= "Armandi",
                                     data_di_nascita= "21/04/1989",
                                     genere= "M",
                                     ore_lavorate= 500,
                                     maretia_insegnata= "PYTHON",
                                     ore_di_lezione= 35)

print(professore1.ore_di_lezione)
print(str(professore1))
# print(dipendente1.name)
# print(dipendente1.calcola_età())
# print(dipendente1.calcola_stipendio())
# print(dipendente1.ore_lavorate)
# print(persona1.calcola_età())
