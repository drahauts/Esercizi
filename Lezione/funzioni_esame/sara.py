"""
Scrivi una funzione che converta una lista di tuple (chiave, valore)
in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già
associata alla chiave.
"""
def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dikty = {}
    for t in tuples:
        key = t[0]
        value = t[1]
        if key in dikty:
            dikty[key].append(value)
        else:
            dikty[key] = [value]
    
    return dikty


# print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))


a = [('a', 1), ('b', 2), ('a', 3)]
print(a)
b = set(a)
print(b)
for l in b:
    print(l)