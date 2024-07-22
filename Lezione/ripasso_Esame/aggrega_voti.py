"""
Scrivi una funzione che prenda in input una lista di dizionari
che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.


Test:                                           Result:                                                                                 

print(aggrega_voti(                             {'Alice': [90, 85], 'Bob': [75]}
[{'nome': 'Alice', 'voto': 90},
{'nome': 'Bob', 'voto': 75},
{'nome': 'Alice', 'voto': 85}]))

"""

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    new_dict = {}
    for v in voti:
        nome = v["nome"]
        voto = v["voto"]
        if nome in new_dict:
            new_dict[nome].append(voto)
        else:
            new_dict[nome] = [voto]

    return new_dict


print(aggrega_voti([{'nome': 'Alice', 'voto': 90},{'nome': 'Bob', 'voto': 75},{'nome': 'Alice', 'voto': 85}]))
