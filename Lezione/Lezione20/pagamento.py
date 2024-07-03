class Pagamento: 
    """
    Si definisca una nuova classe Pagamento che contiene un attributo privato
    e di tipo float che memorizza l'importo del pagamento e si definiscano appropriati
    metodi get() e set(). L'importo non è un parametro da passare in
    input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo
    set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() che visualizza
    una frase che descrive l'importo del pagamento, ad esempio:
    "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.
    """
    
    def __init__(self) -> None:
        self.__importo_pagamento: float = None

    def get_importo(self):
        return self.__importo_pagamento

    def set_importo(self, importo: float):
        if isinstance(importo, float) and importo >= 0:
            self.__importo_pagamento = importo
        else:
            raise ValueError("L'importo deve essere un numero float positivo.")


    def dettagliPagamento(self):
        return f'Importo del pagamento: €{self.__importo_pagamento:.2f}'
    
pagamento = Pagamento()
pagamento.set_importo(40.00)
print(pagamento.dettagliPagamento())

class PagamentoContanti(Pagamento):
    """
    Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento
    e definisca l'importo. Questa classe dovrebbe ridefinire il metodo dettagliPagamento()
    per indicare che il pagamento è in contanti.
    Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote
    da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante
    monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro
    sono necessarie per pagare l'importo in contanti.    
    """

    def __init__(self) -> None:
        super().__init__()

    def dettagliPagamento(self):
        return f'Pagamento in contanti di: €{self.get_importo():.2f}'
    
    def inPezziDa(self):
        cash = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1]
        print(f'{self.get_importo():.2f} euro da pagare in contanti con:')

pagamento_contanti = PagamentoContanti()
pagamento_contanti.set_importo(50.50)
print(pagamento_contanti.dettagliPagamento())
pagamento_contanti.inPezziDa()


class PagamentoCartaDiCredito(Pagamento):
    """
    Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento
    e che definisce l'importo. Questa classe deve contenere gli attributi per il
    nome del titolare della carta, la data di scadenza, e il numero della carta di credito.
    Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni
    della carta di credito oltre all'importo del pagamento.
    """
    def __init__(self, titolare: str, scadenza:str, num_carta: int) -> None:
        super().__init__()
        self.titolare: str = titolare
        self.data_scadenza:str = scadenza
        self.num_carta:int = num_carta

    def dettagliPagamento(self):
        """
        Nome sulla carta: Mario Rossi
        Data di scadenza: 12/24
        Numero della carta: 1234567890123456
        """
        print(
            f'Pagamento di: €{self.get_importo():.2f} effettuato con la carta di credito'
        )
        
        #return f'Pagamento di: €{self.get_importo():.2f} effettuato con la carta di credito\nNome sulla carta: {self.titolare}\nData di scadenza: {self.data_scadenza}\nNumero della carta: {self.num_carta}'
        
    
    


pagamento_carta = PagamentoCartaDiCredito('Marco Rossi', '11/24', 12345661234)
print(pagamento_carta.dettagliPagamento())