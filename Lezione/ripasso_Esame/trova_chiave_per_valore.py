"""
Scrivi una funzione che prenda un dizionario e un valore,
e ritorni la prima chiave che corrisponde a quel valore,
o None se il valore non è presente.

Test:	                                                                        Result:

print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))             b
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))                  None
"""

def trova_chiave_per_valore(my_dict: dict, value: int):
    for k, v in my_dict.items():
        if v == value:
            return k
        
print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'x': 5, 'y': 10, 'z': 15}, 15))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))
print(trova_chiave_per_valore({}, 10))