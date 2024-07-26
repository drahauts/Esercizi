"""
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

Test:                                                   Resutlt:

print(frequency_dict(['mela', 'banana', 'mela']))       {'mela': 2, 'banana': 1}
"""

def frequency_dict(elements: list) -> dict:
    # my_dict: dict = {}
    # for item in elements:
    #     if item in my_dict:
    #         my_dict[item] += 1
    #     else:
    #         my_dict[item] = 1
    
    # return my_dict
    my_Dict = {}
    [my_Dict.update({i: my_Dict.get(i, 0) + 1}) for i in elements]
    return my_Dict


print(frequency_dict(['mela', 'banana', 'mela']))

"""
1100
0111
____
10011
"""