"""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi
e restituisca un nuovo dizionario con solo i prodotti che hanno un
prezzo superiore a 20, scontati del 10%.

Test:                                                                               Result:

print(filtra_e_mappa(                                       
{'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))                                  {'Zaino': 45.0,
                                                                                    'Quaderno': 19.8}
"""

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    new_dict: dict = {}
    for key,value in prodotti.items():
        if value >= 20:
           new_dict[key] = value - (value / 10)

    return new_dict


print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Tavolo': 120.0, 'Sedia': 85.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))
print(filtra_e_mappa({'Lampada': 35.0, 'Libro': 19.0}))
print(filtra_e_mappa({}))