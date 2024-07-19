"""
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario.
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

Test:                                                               Result:

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))           {'a': [1, 3], 'b': [2]}
"""

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dizionario = {}
    for t in tuples:
        key = t[0]
        value = t[1]
        if key in dizionario:
            dizionario[key].append(value)
        else:
            dizionario[key] = [value]

    return dizionario

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))