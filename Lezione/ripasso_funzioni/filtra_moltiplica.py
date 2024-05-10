"""
Scrivi una funzione che riceve una lista di numeri,
filtra i numeri pari, e restituisce una nuova lista
con i numeri pari moltiplicati per un fattore dato.
"""

def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    new_list: list = []    
    for l in lista_numeri:
        if l % 2 == 0:
            l *= fattore
            new_list.append(l)

    return new_list


lista_numeri = [1,2,3,4,5,6]
print(filtra_moltiplica(lista_numeri, 3))


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


"""
Scrivi una funzione che prenda un dizionario e un valore,
e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
"""
def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key, value in dizionario.items():
        if value == valore:
            return key
        

print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))


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


"""
Scrivi una funzione che prenda in input una lista di dizionari
che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
"""

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    for voto in voti:
        print(voto)
    # for k,v in voto.items():
    #     print(k, v)
    
    # for key, value in voto.items():
    #     print(key)
    #     print(value)
aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])