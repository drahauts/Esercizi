import random

<<<<<<< HEAD



ostacoli: dict[int] = {
    15: -3,
    30: - 5,
    45 : -7
    }

bonus: dict[int] = {
    10: 5, 
    23 : 3,
    50: 10
}

def ostacoli(posizione):
    if posizione in ostacoli:
        posizione += ostacoli[posizione]
        if posizione < 1:
            posizione = 1
    elif posizione in bonus:
        posizione += bonus[posizione]
        if posizione > 69:
            posizione = 69
    
    return posizione


def tartaruga(posizione: int, energia, meteo):
    step_T: int = random.randint(1, 10)
    meteo = "sole"
    energia = 100
    
    if 1 <= step_T <= 5:
        posizione += 3
    elif 6 <= step_T <= 7:
        posizione -= 6
=======
def pos_Taruga(posizione: int):
    mossa: int = random.randint(1,10)
    
    if 1 <= mossa <= 5:
        posizione += 3              # Passo veloce (50%): avanza di 3 quadrati
    elif 6 <= mossa <= 7:
        posizione -= 6              # Scivolata (20%): arretra di 6 quadrati
>>>>>>> 9081c67 (lol)
        if posizione < 1:
            posizione = 1           # Non può andare sotto il quadrato 1
    elif 8 <= mossa <= 10:
        posizione += 1              # Passo lento (30%): avanza di 1 quadrato

    return posizione

def lepre(posizione: int):
    mossa: int = random.randint(1, 10)
    
    if 1 <= mossa <= 2:
        pass                        # Riposo (20%): non si muove.
    elif 3 <= mossa <= 4:
        posizione += 9              # Grande balzo (20%): avanza di 9 quadrati.
    elif mossa == 5:
        posizione -= 12             # Grande scivolata (10%): arretra di 12 quadrati.
        if posizione < 1:
            posizione = 1           # Non può andare sotto il quadrato 1.
    elif 6 <= mossa <= 8:
        posizione += 1              # Piccolo balzo (30%): avanza di 1 quadrato.
    elif 8 <= mossa <= 10:
        posizione -= 2              # Piccola scivolata (20%): arretra di 2 quadrati. Non può andare sotto il quadrato 1.
        if posizione < 1:
            posizione = 1

    return posizione

def percorso(mov_Tar, mov_Lep):
    mappa: list = ["_"] * 70

<<<<<<< HEAD
def mappa(mov_t: int, mov_l: int):
    percorso: list = ["_"] * 70

    if mov_t > 69 :
        mov_t = 69
    if mov_l > 69:
        mov_l = 69

    if mov_t == mov_l:
        percorso[mov_t] = "OUCH!!!"
=======
    if mov_Tar > 69:
        mov_Tar = 69
    if mov_Lep > 69:
        mov_Lep = 69
    
    if mov_Tar == mov_Lep:
        mappa[mov_Tar] = "OUCH!!!"
>>>>>>> 9081c67 (lol)
    else:
        mappa[mov_Tar] = "T"
        mappa[mov_Lep] = "H"

    print("".join(mappa))

def gara():
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
    
    pos_T = 1
    lepr = 1
    
    while True:
        pos_T = pos_Taruga(pos_T)
        lepr = lepre(lepr)
        percorso(pos_T, lepr)    
        
        if pos_T >= 69 and lepr >= 69:
            print("IT'S A TIE.")
            break
        elif pos_T >= 69:
            pos_T = 69
            print("TORTOISE WINS! || VAY!!!")
            break
        elif lepr >= 69:
            lepr = 69
            print("HARE WINS || YUCH!!!")
            break

<<<<<<< HEAD
=======
def variabilita_ambientale():
    meteo = "sole"
    count = 0
    pos_T, pos_L = 1, 1

    while True:
        count += 1

        if count % 10 == 0:
            if meteo == "sole":
                meteo = "pioggia"
            else:
                meteo = "sole"

        pos_T = pos_Taruga(pos_T)
        pos_L  = lepre(pos_L)

        if meteo == "pioggia":
            pos_T = pos_T - 1
            if pos_T < 1:
                pos_T = 1
            pos_L = pos_L - 1
            if pos_L < 1:
                pos_L = 1
        percorso(pos_T, pos_L)

        if pos_T >= 69 and pos_L >= 69:
            print("IT'S A TIE.")
            break
        elif pos_T >= 69:
            pos_T = 69
            print("TORTOISE WINS! || VAY!!!")
            break
        elif pos_L >= 69:
            pos_L = 69
            print("HARE WINS || YUCH!!!")
            break

variabilita_ambientale()
>>>>>>> 9081c67 (lol)
