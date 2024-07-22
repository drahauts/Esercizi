"""
Progettare un semplice sistema bancario con i seguenti requisiti:

Classe del Account:
Attributi:
account_id: str - identificatore univoco per l'account.
balance: float - il saldo attuale del conto.
Metodi:
deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
get_balance(): restituisce il saldo corrente del conto.
Classe Bank:
Attributi:
accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
Metodi:
create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
"""

class Account:
    def __init__(self, account_id: str) -> None:
        self.account_id = account_id
        self.balance = 0

    def deposit(self, amount: float):
        """
        Aggiunge l'importo specificato al saldo del conto.
        """
        self.balance += amount
        print(f"L'importo {amount} e stati aggiunto corretamente. Il saldo attuale: {self.balance}")
    
    def get_balance(self):
        return f"Il saldo corrente: {self.balance}"
    
class Bank:
    def __init__(self) -> None:
        self.accounts:dict[str, Account] = {}
    
    def create_account(self, account_id):
        if account_id not in self.accounts:
            self.accounts[account_id] = Account(account_id)
        else:
            return f"Errore, account già esiste."

    
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
        else:
            print(f"Errore: account con ID {account_id} non esiste.")

        
    def get_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
        else:
            return f"Acount con ID {account_id} non esiste."
        

bank = Bank()
bank.create_account("123")