"""
Dato un stringa s che consiste di lettere minuscole o maiuscole,
scrivi una funzione che restituisca la lunghezza del palindromo più
lungo che può essere costruito con quelle lettere. Le lettere sono
sensibili al caso, ad esempio, "Aa" non è considerato un palindromo qui.
"""

def longest_palindrome(s: str) -> int:
    my_dict: dict = {}

    for key in s:
        if key not in my_dict:
            my_dict[key] = 1
        elif key in my_dict:
            my_dict[key] += 1
    print(my_dict)

    count = 0
    count_dispari = False

    for value in my_dict.values():
        if value % 2 == 0:
            count += value
        else:
            count += value - 1
            count_dispari = True
        # if value == 1:
        #     count = 1

    if count_dispari:
        count += 1
    
    return count 

print(longest_palindrome("abccccdd"))