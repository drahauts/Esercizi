"""
Dato una stringa s che contiene solo i caratteri

'(', ')', '{', '}', '[' e ']',

scrivi una funzione per determinare se la stringa di input è valida.
Una stringa di input è valida se:

Le parentesi aperte devono essere chiuse dallo stesso tipo di parentesi.
Le parentesi aperte devono essere chiuse nell'ordine corretto.
Ogni parentesi chiusa deve avere una parentesi aperta corrispondente dello stesso tipo.

Test:                                               Result:

print(is_valid_parenthesis("()"))                   True

"""
def is_valid_parenthesis(s: str) -> bool:
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")

    if len(s) == 0:
        return True
    else:
        return False
    
print(is_valid_parenthesis("()"))