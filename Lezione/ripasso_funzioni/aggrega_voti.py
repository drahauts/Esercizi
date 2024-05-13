"""
Scrivi una funzione che prenda in input una lista di dizionari
che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
"""

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    nuovo_registro: dict = {}

    for studente in voti:
        nome = studente["name"]
        voto = studente["voto"]

        if nome in nuovo_registro:
            nuovo_registro[nome].append(voto)
        else:
            nuovo_registro[nome] = [voto]


aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])