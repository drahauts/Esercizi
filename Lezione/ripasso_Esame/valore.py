"""
Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
"""

def valore(my_list: list[int]):
    return f"Valore massimo: {max(my_list)},\nValore minimo: {min(my_list)},\nValore medio: {sum(my_list) / len(my_list):.2f}"


lista = [12, 42, 14, 4, 1, 53, 16, 72, 34]
print(valore(lista))