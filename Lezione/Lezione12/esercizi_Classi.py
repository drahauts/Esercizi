"""
Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema.
Il cinema ha diverse sale, ognuna con un diverso film in programmazione.
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
"""

class Film:
    

    def __init__(self, titolo: str, durata: float) -> None:
        self.titolo = titolo
        self.durata = durata

    
    def __str__(self) -> str:
        return f"Film(titolo: {self.titolo}, durata: {self.durata})"

film_1 = Film(titolo= "Bella e Bestia", durata= 1.53)
print(film_1)

class Sala:

    def __init__(self, num_sala: int, film: Film, posti_totali: int) -> None:
        self.num_sala = num_sala
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti):
        self.posti_totali -= num_posti


        if self.posti_totali > 0:
            return f"La tua prenotazione è confermata."
        else:
            return f"Errore. La sala è piena."
        
    def posti_disponibili(self):
        if self.posti_totali - self.posti_prenotati < 0:
            return  f"Non ci sono più posti disponibili"
        else:
            return f"Posti ancora disponibili: {self.posti_totali - self.posti_prenotati}"
    
    def __str__(self) -> str:
        return f"Sala(num_sala: {self.num_sala}, film: {self.film}, posti_totali: {self.posti_totali})"
    

sala1 = Sala(num_sala = 4, film= film_1, posti_totali= 100)
#print(sala1)
print(sala1.prenota_posti(43))
print(sala1.posti_disponibili())


"""
aggiungi_sala(sala): Aggiunge una nuova sala al cinema.

prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti.
    Restituisce un messaggio di stato.
"""
class Cinema:

    def __init__(self) -> None:
        self.sala:list[Sala] = []
        self.titolo_film: Film = Film

    def add_sala(self, sala):
        self.sala.append(sala)
        return self.sala
    
    def prenota_film(self, titolo_film: Film, num_posti: Sala):
        
        
        pass
        
    def __str__(self) -> str:
        return f"Cinema(sala: {self.sala}, titolo: {self.titolo_film})"
    

cinema1 = Cinema()
print(cinema1.add_sala(sala= ["sala1", "sala3", "sala_4"]))

