def length_of_last_world(s:str) -> int:
    world = s.split()
    print(world)
    return len(world[-1])
    

print(length_of_last_world("    ke  k lol ciao ciao danila    "))


"""
data una stringa che contiene parole e spazzi, restituire la lunghezza dell'ultima parola in s.

una parola è una sottostringa che contiene caratteri contigui diversi dallo spazio

"""