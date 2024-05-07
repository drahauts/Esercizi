"""
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

________________________________________________________________

Test	                                           Result 

print(merge_dictionaries({'x': 5}, {'x': -5}))     {'x': 0}
_________________________________________________________________
"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value

    return dict1

	
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dictionaries({}, {'a': 10, 'b': 20}))
print(merge_dictionaries({'x': 5}, {'x': -5}))