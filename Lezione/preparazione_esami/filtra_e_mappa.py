"""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario
con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.


Test:                                                                           Result:

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))         {'Zaino': 45.0, 'Quaderno': 19.8}
"""

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    # new_d = {}
    # for k, v in prodotti.items():
    #     if v >= 20:
    #         new_d[k] = v - (v / 10)

    # return new_d
    new_d = {k: v - (v/10) for k,v in prodotti.items() if v >= 20}
    
    return new_d

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))