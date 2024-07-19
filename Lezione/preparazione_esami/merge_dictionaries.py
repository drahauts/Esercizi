"""
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

Test:                                                       Result:

print(merge_dictionaries({'x': 5}, {'x': -5}))              {'x': 0}
"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    new_dict = dict1

    for k,v in dict2.items():
        if k in new_dict:
            new_dict[k] += v
        else:
            new_dict[k] = v
    
    return new_dict

print(merge_dictionaries({'x': 5}, {'x': -5}))

