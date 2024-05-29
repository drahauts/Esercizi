class Banca:

    def __init__(self, nome: str, simbolo: str) -> None:
        
        self.nome: str = nome
        self.simbolo: str = simbolo
        self.lista_filiali: list[Filiale] = []

    def numero_filiali(self):
        
        return len(self.lista_filiali)


class Filiale:

    filiali_creati = 0

    def __init__(self, codice: str, indirizzo: str, banca: Banca) -> None:
        
        self.codice:str = codice
        self.indirizzo: str = indirizzo
        self.banca: Banca = banca

        Filiale.filiali_creati += 1

    @classmethod
    def totale_filiali_create(cls):
        return cls.filiali_creati

uniCredit: Banca = Banca(nome= "UniCredit", simbolo= "UCG")
intesa: Banca = Banca(nome= "Intesa San Paolo", simbolo= "ISP")

filiale_unicredit_1: Filiale = Filiale(codice= "UCG01",
                                       indirizzo= "Via Sierra Nevada 60, Roma, Italia",
                                       banca=uniCredit)

filiale_intesa_1: Filiale = Filiale(codice= "ISP01",
                                    indirizzo= "Piazza Barberini, 60, Roma, Italia",
                                    banca= intesa)


uniCredit.lista_filiali.append(filiale_unicredit_1)
intesa.lista_filiali.append(filiale_intesa_1)

print(filiale_unicredit_1.banca.nome)