from abc import ABC, abstractmethod

class Volo(ABC):
    """
    il codice del volo (stringa)
    la capacità massima di posti disponibili sul volo (numero intero)
    che sono attributi passati come argomenti in input.
    
    Inoltre, la classe deve avere un attributo chiamato prenotazioni,
    il quale non deve essere passato come argomento del costruttore;
    il costruttore, però, deve assegnare valore iniziale pari a 0 a tale attributo.
    """
    def __init__(self, codice_volo:str, posti_disponibili_volo: int) -> None:
        self.codice_volo = codice_volo
        self.posti_disponibili_volo = posti_disponibili_volo
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto(self):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass


class VoloCommerciale(Volo):
    """
    Estende la classe Volo e definisce gli attributi codice del volo e capacità massima di posti disponibili sul volo.
    Il costruttore deve inoltre gestire i seguenti attributi interi: posti_economica, posti_business, e posti_prima;
    i quali consentono di stabilire quanti posti sono stati riservati alla classe economica, quanti alla classe
    business e quanti alla prima classe su ogni volo. Il costruttore non deve ricevere in input questi argomenti,
    ma assegnare loro un valore iniziale tale che la somma di questi tre valori interi sia uguale al numero dei posti
    disponibili sul volo. Si può pensare di riservare il 70% dei posti alla classe economica, il 20% dei posti alla
    classe business ed i restanti posti alla prima classe. Inoltre, il costruttore deve creare tre valori interi pari a 0,
    chiamati prenotazioni_economica, prenotazioni_business, prenotazioni_prima.
    """
    def __init__(self, codice_volo: str, posti_disponibili_volo: int) -> None:
        super().__init__(codice_volo, posti_disponibili_volo)
        self.posti_economica_riservati = (posti_disponibili_volo * 0.7)
        self.posti_business_riservati = (posti_disponibili_volo * 0.2)
        self.posti_prima_riservati =  posti_disponibili_volo - (self.posti_economica_riservati + self.posti_business_riservati)
        self.posti_economica: int = 0
        self.posti_business: int = 0
        self.posti_prima: int = 0

    def prenota_posto(self, posti, classe_servizio):
        """
        prenota_posto(posti, classe_servizio): che consente di prenotare un certo numero di posti sul volo in una determinata classe.
        Tale metodo, prima di riservare un posto, deve controllare prima che ci siano posti disponibili sull'intero volo,
        poi se ci sono posti disponibili nella classe richiesta. In caso affermativo, contare il numero dei posti prenotati in tale classe.
        Inoltre, nel caso in cui sia possibile prenotare un posto, il metodo deve stampare a schermo un messaggio che notifichi all'utente
        di aver riservato un tot di posti per una determinata classe su un dato volo (specificando il codice del volo). In caso contrario,
        stampare a schermo un messaggio che notifichi all'utente che non ci sono più posti disponibili nella classe scelta. Se sul volo non ci sono
        più posti disponibili, il metodo deve stampare a schermo un messaggio notificando all'utente che il volo è al completo.
        Inoltre, se la classe passata come input del metodo non risulta essere una delle seguenti classi ("economica", "business", "prima"),
        il metodo deve stamapre a schermo un messaggio di errore, notificando all'utente che la classe richiesta non è valida.
        Infine, il metodo deve aggiornare l'attributo prenotazioni della classe estesa Volo, sommando il numero di prenotazioni ricevute
        per ogni classe di servizio, poi aggiornare gli attributi prenotazioni_economica, prenotazioni_business, prenotazioni_prima con
        l'esatto numero delle prenotaioni ricevute per ogni classe di servizio. Suggerimento: introdurre delle variabili locali d'appoggio
        per gestire le prenotazioni per ogni classe di servizio da azzerare all'inizio di ogni fase di prenotazione.
        """
        if posti in self.posti_disponibili_volo and (classe_servizio in self.posti_business_riservati) or (classe_servizio in self.posti_economica_riservati) or (classe_servizio in self.posti_prima_riservati):
            pass

        if posti<=self.posti_disponibili_volo and ((classe_servizio=="econimica" and posti<=self.posti_economica) or (classe_servizio=="business" and posti<=self.posti_business) or (classe_servizio=="prima" and posti<=self.posti_prima)):
            pass