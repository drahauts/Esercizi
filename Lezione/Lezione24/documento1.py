class Documento:

    def __init__(self, testo: str) -> None:
        self.testo: str = testo

    def getText(self):
        return self.testo

    def setText(self, new_testo: str):
        self.testo = new_testo

    def islnText(self, parola_chiave: str):
        if parola_chiave.lower() in self.testo.lower():
            return True
        else:
            return False


class Email(Documento):

    def __init__(self, testo: str, mittente: str, destinatario: str, titolo: str) -> None:
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo

    def getMittente(self):
        return self.mittente

    def getDest(self):
        return self.destinatario

    def getTitolo(self):
        return self.titolo

    def setTesto(self, new_testo: str):
        self.testo = new_testo

    def setMittente(self, new_mitt: str):
        self.mittente = new_mitt

    def setDest(self, new_dest: str):
        self.destinatario = new_dest

    def setTitolo(self, new_t: str):
        self.titolo = new_t

    def getText(self):
        return f'Da {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessagio: {self.testo}'

    def writeToFile(self):
        with open(file='email1.txt', mode='w') as caso:
            caso.write(self.getText())


documento1 = Documento("Comunque adesso ho un po' paura!")
print(documento1.getText())
documento1.setText('Creatura')
print(documento1.islnText("creatura"))


email = Email('Ciaone', 'danilarogowzow@gmail.com',
              "sara00gmail.com", 'Incontro')
email.setTesto('Compra/Vendita')
email.setDest('milonino@gmail.com')
email.setMittente('danilaraha@gmail.com')
email.setTitolo('Cane')
print(email.getText())
email.setDest('oussama@libero.it')
email.setTesto('Una partitina veloce a poker?')
email.setTitolo('Poker?')
print(email.getText())
email.writeToFile()
