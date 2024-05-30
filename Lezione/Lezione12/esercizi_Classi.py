"""
Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema.
Il cinema ha diverse sale, ognuna con un diverso film in programmazione.
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
"""

class Film:
    

    def __init__(self,film: str, titolo: str, durata: float) -> None:
        self.film = film
        self.titolo = titolo
        self.durata = durata

    
    def __str__(self) -> str:
        return f"Film(film: {self.film}, titolo: {self.titolo}, durata: {self.durata})"

film_1 = Film(film= "Bella e Bestia", titolo= "Una storia vera che parla di...", durata= 1.53)
print(film_1)

class Sala:

    def __init__(self, num_sala: int, film: Film, posti_totali: int) -> None:
        self.num_sala = num_sala
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti):
        self.posti_totali -= num_posti


        if self.posti_totali != 0:
            return f"La tua prenotazione è confermata."
        else:
            return f"Errore. La sala è piena."
        
    def posti_disponibili(self):
        return f"Posti ancora disponibili: {self.posti_totali - self.posti_prenotati}"
    
    def __str__(self) -> str:
        return f"Sala(num_sala: {self.num_sala}, film: {self.film}, posti_totali: {self.posti_totali})"
    

sala1 = Sala(num_sala = 4, film= film_1, posti_totali= 100)
print(sala1.prenota_posti(4))
print(sala1.posti_disponibili())