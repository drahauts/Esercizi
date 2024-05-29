class ContoBancario():

    total_accounts = 0

    def __init__(self, iban: int, saldo: int, nome: str) -> None:
        self.iban = iban
        self.saldo = saldo
        self.nome = nome

        ContoBancario.total_accounts += 1

    def deposito(self, importo: int):
        self.saldo += importo
        print(f"{importo} depositato. Il nuovo saldo è {self.saldo}")
    
    def prelievo(self, importo: int):
        self.saldo -= importo
        print(f"{importo} prelevato. Il nuovo saldo è {self.saldo}")

    
    @classmethod
    def get_total_accounts(cls):
        print(f"Account totali creati: {cls.total_accounts}")

    @staticmethod
    def valida_account(iban):
        if isinstance(iban, int) and len(str(iban)) == 10:
            print("iban valido")
            return True
        else:
            print("iban non valido")
            return False
        

account_1 = ContoBancario(1234567890, 0, "Pluto")
account_2 = ContoBancario(1122334455, 12000, "Pippo")

account_1.deposito(5000)
account_1.prelievo(10)

account_2.deposito(25000)
account_2.prelievo(500)

ContoBancario.get_total_accounts()

account_3 = ContoBancario(1234567890, 0, "Pluto") 

ContoBancario.get_total_accounts()
ContoBancario.valida_account(1234567890)
ContoBancario.valida_account("123456789")

