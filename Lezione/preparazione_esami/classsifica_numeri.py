"""
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica
i numeri in liste separate per numeri pari e dispari.


Test:                                                   Result:

print(classifica_numeri([1, 2, 3, 4, 5, 6]))            {'pari': [2, 4, 6], 'dispari': [1, 3, 5]}
"""

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    d = {'pari' : [],
     'dispari' : []}
    for l in lista:
        if l % 2 == 0:
            d['pari'].append(l)
        else:
            d['dispari'].append(l)

    return d

print(classifica_numeri([1, 2, 3, 4, 5, 6]))