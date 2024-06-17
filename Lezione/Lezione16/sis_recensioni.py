class Media:

    def __init__(self, title: str, reviews: list[int]) -> None:
        self.title = title
        self.reviews = reviews

    def set_title(self, title: str):
        self.title = title
    
    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto: int):
        """
        Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5)
        """
        if 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            return f'Errore. Hai scritto il valore sbagliato {voto}'
    
    def getMedia(self):
        """
        Calcola e restituisce la media delle valutazioni.
        """        
        return round((sum(self.reviews) / len(self.reviews)))
    
    def getRate(self):
        """
        Restituisce una stringa che descrive il giudizio medio basato
        sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina a 1,
        "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3,
        "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
        """
        if self.getMedia() == 1:
            print(f'Terribile')
        elif self.getMedia() == 2:
            print('Brutto')
        elif self.getMedia() == 3:
            print('Normale')
        elif self.getMedia() == 4:
            print('Bello')
        elif self.getMedia() == 5:
            print('Grandioso')

    def ratePercentage(self, voto: int):
        """
        Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
        """
        if len(self.reviews) > 0:
            count = self.reviews.count(voto)
            return count / len(self.reviews) * 100
        else:
            return f'Errore'


media = Media('Lol', [1, 3, 5, 5, 5, 5, 4, 2])
print(media.getMedia())
media.getRate()
print(media.ratePercentage(5))