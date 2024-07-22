"""
Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando le
lettere di una parola o frase diversa, in genere utilizzando
tutte le lettere originali esattamente una volta.


Test:                                           Result:

print(anagram("anagram","nagaram"))             True

"""
def check_anagram(my_string: str):
    my_dict: dict = {}
    for ms in my_string.lower():
        if ms in my_dict:
            my_dict[ms] += 1
        else:
            my_dict[ms] = 1
        
    return sorted(my_dict.items())

def anagram(str1: str, t1: str) -> bool:
    return check_anagram(str1) == check_anagram(t1)

print(anagram("anagram","nagaram"))
print(anagram("rat","cat"))
print(anagram("silent","listen"))
print(anagram("NeurIPS","UniReps")) 
