"""
Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

Test:                                               Result:

print(sum_above_threshold([15, 5, 25], 20))         25
"""

def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    somma = 0
    for n in numbers:
        if n > threshold:
            somma += n
    
    return somma
    


print(sum_above_threshold([15, 5, 25], 20))
print(sum_above_threshold([1, 10, 20, 30], 10))