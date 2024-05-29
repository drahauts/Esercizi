import random

def tartaruga(posizione: int):
    step_T: int = random.randint(1, 10)
    # print(f"Tartaruga = {step_T}")
    if 1 <= step_T <= 5:
        posizione += 3
    elif 6 <= step_T <= 7:
        posizione -= 6
        if posizione < 1:
            posizione = 1
    elif 8 <= step_T <= 10:
        posizione += 1

    return posizione

def lapre(posizione: int):
    step_L: int = random.randint(1, 10)
    # print(f"Lepre = {step_L}")
    if 1 <= step_L <= 2:
        pass
    elif 3 <= step_L <= 4:
        posizione += 9
    elif step_L == 5:
        posizione -= 12
        if posizione < 1:
            posizione = 1
    elif 6 <= step_L <= 8:
        posizione += 1
    elif 9 <= step_L <= 10:
        posizione -= 2
        if posizione < 1:
            posizione = 1

    return posizione


def mappa(mov_t: int, mov_l: int):
    percorso: list = ["_"] * 70

    if mov_t > 69:
        mov_t = 69
    if mov_l > 69:
        mov_l = 69

    if mov_t == mov_l:
        percorso[mov_t] = "OUCH!!!"
    else:
        percorso[mov_t] = "T"
        percorso[mov_l] = "H"

    print("".join(percorso))


def gara():
    print(" " * 30, "'BANG !!!!! AND THEY'RE OFF !!!!!'")

    mossa_Tart = 1
    mossa_Lepr = 1

    while True:
        mossa_Tart = tartaruga(mossa_Tart)
        mossa_Lepr = lapre(mossa_Lepr)
        mappa(mossa_Tart, mossa_Lepr)
        # print(f"Posizione di tartaruga e {mossa_Tart}, lepra {mossa_Lepr}", "\n", "===" * 30)
        if mossa_Tart >= 69 and mossa_Lepr >= 69:
            print("IT'S A TIE.")
            break
        elif mossa_Tart >= 69:
            mossa_Tart = 69
            print("\n"* 2 ,"TORTOISE WINS! || VAY!!!")
            break
        elif mossa_Lepr >= 69:
            mossa_Lepr = 69
            print("\n" * 2, "HARE WINS || YUCH!!!")
            break


gara()