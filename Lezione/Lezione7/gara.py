import random

def tartaruga(posizione: int):
    movim_tart: int = random.randint(1,10)
    # print("tartaruga: ", movim_tart)
    if 1 <= movim_tart <= 5:
        posizione += 3          # Passo veloce (50%): avanza di 3 quadrati.
    elif 6 <= movim_tart <= 7:
        posizione -= 6          # Scivolata (20%): arretra di 6 quadrati.
    elif 8 <= movim_tart <= 10:
        posizione += 1          # Passo lento (30%): avanza di 1 quadrato

    return max(1, posizione)




def lepre(posizione: int):
    movim_lepre: int = random.randint(1,10)
    # print("lepre: ",movim_lepre,"\n", "#" * 70)
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


def mappa(mossa_tart: int, mossa_lep: int):
    # corsa: list = ['_' for _ in range(0, 70)]
    corsa: list = ["_"] * 70
    if mossa_tart == mossa_lep:
        corsa[mossa_lep] = "OUCH!!!"    # Se la posizione e uguale
    else:
        corsa[mossa_tart] = 'T'         # TARTARUGA
        # print("posizione della tartaruga: ", mossa_tart)
        corsa[mossa_lep] = 'H'          # LEPRA
        # print("posizione della lepre: ", mossa_lep)
        print('=' * 70)

    print('-'.join(corsa))
    # print(corsa)

# mappa(mossa_tart= 69, mossa_lep= 68)
# mappa(mossa_tart= 0, mossa_lep= 1)
# mappa(mossa_tart= 1, mossa_lep= 2)

def gara():
    print(" "* 25, "BANG !!!!! AND THEY'RE OFF !!!!!")
    pos_tart = 1
    pos_lep = 1

    while True:
        pos_tart = tartaruga(pos_tart)
        pos_lep = lepre(pos_lep)
        mappa(pos_tart, pos_lep)
        print("posizioni l: ", pos_lep,"\npos Tart: " ,pos_tart)

        if pos_tart >= 69 and pos_lep >= 69:
            print("IT'S A TIE.")
            break
        elif pos_tart >= 69:
            pos_tart = 69
            print("TORTOISE WINS! || VAY!!!")
            break
        elif pos_lep >= 69:
            pos_lep = 69
            print("HARE WINS || YUCH!!!")
            break

gara()