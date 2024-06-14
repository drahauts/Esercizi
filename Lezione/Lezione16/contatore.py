class Contatore:

    def __init__(self, counter: int = 0) -> None:
        self.count = counter

    def setZero(self):
        self.count = 0

    def add1(self):
        self.count += 1

    def sub1(self):
        if self.count <= 0:
            print("Non è possibile eseguire la sottrazione")
        else:
            self.count -= 1
    
    def get(self):
        return self.count
    
    def mostra(self):
        print(f'Conteggio attuale: {self.count}')

c = Contatore()  
c.sub1()  
c.mostra()