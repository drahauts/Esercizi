"""
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
__________________________________________________________________________________

Test	                                                  Result 

print(frequency_dict(['mela', 'banana', 'mela']))         {'mela': 2, 'banana': 1}
___________________________________________________________________________________
"""

def frequency_dict(elements: list) -> dict:
    frequenza: dict = {}
    for element in elements:
        if element in frequenza:
            frequenza[element] += 1
        else:
            frequenza[element] = 1
    
    return frequenza
 
print(frequency_dict(['mela', 'banana', 'mela']))               # {'mela': 2, 'banana': 1}
print(frequency_dict([1, 2, 2, 3, 3, 3]))                       # {1: 1, 2: 2, 3: 3}
print(frequency_dict([]))                                       # {}
print(frequency_dict(['a', 'b', 'c', 'a', 'b', 'c', 'a']))      # {'a': 3, 'b': 2, 'c': 2}
print(frequency_dict([True, False, True]))                      # {True: 2, False: 1}