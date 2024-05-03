"""
Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
________________________________________________________________

Test	                                           Result 

print(list_statistics([1, 2, 3, 4, 5]))            (5, 1, 3.0)
_________________________________________________________________
"""

def list_statistics(numbers: list[int]):
    return max(numbers), min(numbers), sum(numbers) / len(numbers)

print(list_statistics([1, 2, 3, 4, 5]))
print(list_statistics([10, 20, 30, 40, 50]))
print(list_statistics([-5, -1, -3]))
print(list_statistics([2]))
print(list_statistics([1, 1, 1, 1, 2]))