"""
Progettare un semplice sistema bancario con i seguenti requisiti:
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato
"""
class Account:
    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id = account_id
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
    
class Bank:
    def __init__(self) -> None:
        self.accounts = {}
    
    def create_account(self, account_id):
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists")
        self.accounts[account_id] = Account(account_id, balance= 0)
        return self.accounts[account_id]
    
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
        return account_id,
    
    def get_balance(self, account_id):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_id].get_balance()



bank = Bank()
account1 = bank.create_account("123")
try:
    bank.create_account("123")
except ValueError as e:
    print(e)
"""
Account with this ID already exists
"""