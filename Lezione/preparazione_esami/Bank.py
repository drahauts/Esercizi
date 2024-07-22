"""
Progettare un semplice sistema bancario con i seguenti requisiti:
Classe Bank:

accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
Metodi:
create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
"""

class Account:
    """
    account_id: str - identificatore univoco per l'account.
    balance: float - il saldo attuale del conto.
    """
    def __init__(self, account_id, balance = 0) -> None:
        self.account_id = account_id
        self.balance : float = balance
    
    def deposit(self, amount: float):
        """
        deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
        """
        if amount < 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount

    def get_balance(self):
        """
        get_balance(): restituisce il saldo corrente del conto.
        """
        return self.balance

class Bank:
    """
    accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
    """
    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}

    def create_account(self, account_id: str):
        """
        create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
        """
        if account_id in self.accounts:
            raise ValueError('Account with this ID already exists')
        new_Account = Account(account_id)
        self.accounts[account_id] = new_Account
        return new_Account

    def deposit(self, account_id: str, amount: float):
        """
        deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
        """
        if account_id not in self.accounts:
            raise ValueError('Account not found')
        self.accounts[account_id].deposit(amount)
                
    def get_balance(self, account_id: str):
        """
        get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
        """
        if account_id not in self.accounts:
            raise ValueError('Account not found')
        return self.accounts[account_id].get_balance()
        

bank = Bank()
account1 = bank.create_account("123")
try:
    bank.create_account("123")
except ValueError as e:
    print(e)