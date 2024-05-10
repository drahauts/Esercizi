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