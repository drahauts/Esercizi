"""
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
"""


def check_parentheses(expression: str) -> bool:
    lista: list = []
    for char in expression:
        if char == "(":
            lista.append(char)
        elif char == ")":
            if not lista:
                return False
            lista.pop()
    
    return not lista
            
    

print(check_parentheses("Ciao(co(me) stai"))