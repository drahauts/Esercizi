"""
Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

__________________________________________________________________________________

Test	                                                  Result 

print(remove_duplicates([1, 2, 3, 1, 2, 4]))              [1, 2, 3, 4]
___________________________________________________________________________________
"""

def remove_duplicates(lista: list) -> list:
    my_set = set()
    no_duplicates: list = []
    for elem in lista:
        print(f"Il mio elem adesso e - {elem}")
        print(f"Il mio set adesso e -{my_set}")
        if elem not in my_set:
            my_set.add(elem)
            no_duplicates.append(elem)
        
    return no_duplicates

print(remove_duplicates([1, 2, 3, 1, 2, 4]))
print(remove_duplicates([4, 5, 'a', 4, 6]))
print(remove_duplicates(['a', 'b', 'a']))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([]))