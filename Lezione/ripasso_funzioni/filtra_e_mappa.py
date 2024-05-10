"""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un
prezzo superiore a 20, scontati del 10%.
"""

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    new_dict: dict[str:float] = {}
    for key, value in prodotti.items():
        if value > 20:
            sconto = (value * 10) / 100
            value -= sconto
            new_dict[key] = value
    
    return new_dict


prodotti = {'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}
print(filtra_e_mappa(prodotti))