import random

def tartaruga(posizione: int):
    movim_tart: int = random.randint(1,10)

    if 1 <= movim_tart <= 5:
        posizione += 3          # Passo veloce (50%): avanza di 3 quadrati.
    elif 6 <= movim_tart <= 7:
        posizione -= 6          # Scivolata (20%): arretra di 6 quadrati.
    elif 8 <= movim_tart <= 10:
        posizione += 1          # Passo lento (30%): avanza di 1 quadrato

    return max(1, posizione)

def lepre(posizione: int):
    movim_lepre: int = random.randint(1,10)

    if 1<= movim_lepre <= 2:
        pass                    # Riposo (20%): non si muove
    elif 3 <= movim_lepre <= 4:
        posizione += 9          # Grande balzo (20%): avanza di 9 quadrati.
    elif movim_lepre == 5:
        posizione -= 12         # Grande scivolata (10%): arretra di 12 quadrati.
    elif 6 <= movim_lepre <= 8:
        posizione += 1          # Piccolo balzo (30%): avanza di 1 quadrato.
    elif 9 <= movim_lepre <= 10:
        posizione -= 2          # Piccola scivolata (20%): arretra di 2 quadrati.

    return max(1, posizione)


"""
Crea una funzione che stampa una lista di 70 posizioni.
Inserisci la lettera 'T' alla posizione della tartaruga, la lettera 'H' alla posizione della lepre, e il carattere '_' nelle posizioni libere.
Se entrambi gli animali si trovano sulla stessa posizione, stampa 'OUCH!!!' in quella posizione.

Inizializza la corsia: Crea una lista di 70 elementi, tutti impostati su _.
"""

def mappa(mossa_tart: int, mossa_lep: int):
    corsa: list[int] = ['_' for _ in range(70)]

    if mossa_tart == mossa_lep:
        corsa[mossa_lep - 1] = "OUCH!!!"    # Se la posizione e uguale
    else:
        corsa[mossa_lep - 1] = 'H'          # LEPRA
        corsa[mossa_tart - 1] = 'T'         # TARTARUGA

    print(''.join(corsa))


def gara():
    print("BANG !!!!! AND THEY'RE OFF !!!!!")