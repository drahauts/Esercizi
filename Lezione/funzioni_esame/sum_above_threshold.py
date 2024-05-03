"""
Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
________________________________________________________________

Test	                                           Result 

print(sum_above_threshold([15, 5, 25], 20))        25
_________________________________________________________________
"""

def sum_above_threshold(numbers: list[int], threshold: int):
    totale = 0
    for num in numbers:
        if num > threshold:
            totale += num
    
    return totale

print(sum_above_threshold([15, 5, 25], 20))
print(sum_above_threshold([1, 10, 20, 30], 10))
print(sum_above_threshold([3, 5, 8], 10))
print(sum_above_threshold([50, 60, 70], 25))
print(sum_above_threshold([2, 5, 1], 1))