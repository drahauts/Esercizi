"""
Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte.
Ogni carta ha un valore compreso tra 2 e 11 compresi. Tuttavia, se una mano contiene un asso,
il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in quel momento.
Dato un elenco di valori delle carte che rappresentano una mano di blackjack, scrivi una
funzione per determinare il valore totale della mano.
"""
def blackjack_hand_total(cards: list[int]) -> int:
    count = 0
    for card in cards:
        if count + card <= 21:
            count += card
        else:
            card = 1
            count += card
    return count

print(blackjack_hand_total([1, 10, 11]))