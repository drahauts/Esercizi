"""
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un
numero specificato k di posizioni. La rotazione verso sinistra significa che
ciascun elemento della lista viene spostato a sinistra di una posizione e
l'elemento iniziale viene spostato alla fine della lista.

Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

________________________________________________________________

Test	                                           Result 

print(rotate_left([1, 2, 3, 4, 5], 2))             [3, 4, 5, 1, 2]
_________________________________________________________________
"""

def rotate_left(elements: list, k: int) -> list:
    if k > len(elements):
        k = k % len(elements)
    
    return elements[k : ] + elements[ : k]


print(rotate_left([1, 2, 3, 4, 5], 2))
print(rotate_left([5, 3, 7, 2, 1, 4], 8))
print(rotate_left([5, 1], 2))
