"""
Scrivi una funzione che elimini dalla lista dati certi elementi specificati
in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e
il numero di volte che devono essere rimossi come valori.

Test:                                                       Result:

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))            [1, 3, 4]
print(rimuovi_elementi([], {2: 1}))                         []
"""

def rimuovi_elementi(lista: list, my_dict: dict):
    for k, v in my_dict.items():
        while v > 0:
            if k in lista:
                lista.remove(k)
                v -= 1
            else:
                return lista
    
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))
print(rimuovi_elementi([4, 5, 6], {1: 3}))
print(rimuovi_elementi([], {2: 1}))
"""
    return [l * fattore for l in my_list if l % 2 == 0]
"""