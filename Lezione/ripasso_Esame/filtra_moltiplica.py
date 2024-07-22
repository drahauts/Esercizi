"""
Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari,
e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.

Test                                                    Result

print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))         [6, 12, 18]

print(filtra_moltiplica([], 3))                         []
"""

def filtra_moltiplica(my_list: list[int], fattore: int):
    """
    new_list: list = []    
    for l in lista_numeri:
        if l % 2 == 0:
            l *= fattore
            new_list.append(l)

    return new_list
    """
    return [l * fattore for l in my_list if l % 2 == 0]

print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))
print(filtra_moltiplica([2, 4, 6, 8], 2))
print(filtra_moltiplica([1, 3, 5], 10))
print(filtra_moltiplica([10, 20, 30, 40], 5))
print(filtra_moltiplica([], 3))