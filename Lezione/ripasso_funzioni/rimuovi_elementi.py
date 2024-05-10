"""
Scrivi una funzione che elimini dalla lista dati certi elementi specificati
in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi
e il numero di volte che devono essere rimossi come valori.
"""

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    # new_list: list[int] = lista.copy()
    for key, value in da_rimuovere.items():
        while value > 0:
            if key in lista:
                lista.remove(key)
                value -= 1
            else:
                return lista

    return lista

#print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
#print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))