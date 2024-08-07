"""
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica
i numeri in liste separate per numeri pari e dispari.


Test:                                                   Result:

print(classifica_numeri([1, 2, 3, 4, 5, 6]))            {'pari': [2, 4, 6], 'dispari': [1, 3, 5]}
"""

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    # dict_d = {
    #     'pari' : [],
    #     'dispari' : []
    # }
    # for l in lista:
    #     if l % 2 == 0:
    #         dict_d['pari'].append(l)
    #     else:
    #         dict_d['dispari'].append(l)
    
    # return dict_d
    dict_d = {
        'pari' : [l for l in lista if l % 2 == 0],
        'dispari' : [l for l in lista if l % 2 != 0]}

    return dict_d

print(classifica_numeri([1, 2, 3, 4, 5, 6]))