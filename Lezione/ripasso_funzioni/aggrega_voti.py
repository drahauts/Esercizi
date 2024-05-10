"""
Scrivi una funzione che prenda in input una lista di dizionari
che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
"""

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    for voto in voti:
        print(voto)
    # for k,v in voto.items():
    #     print(k, v)
    
    # for key, value in voto.items():
    #     print(key)
    #     print(value)
aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])