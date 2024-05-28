"""
"Dato una stringa s contenente solo i caratteri '(', ')', '{', '}', '[' e ']', scrivi una funzione per determinare se la stringa di input è valida.

Una stringa di input è valida se:

    Le parentesi aperte devono essere chiuse dallo stesso tipo di parentesi.
    Le parentesi aperte devono essere chiuse nell'ordine corretto.
    Ogni parentesi chiusa ha una parentesi aperta corrispondente dello stesso tipo."
"""

def is_valid_parenthesis(s: str) -> bool:
    # my_dict: dict[str] = {
    #     "(" : ")",
    #     "[" : "]",
    #     "{" : "}"
    # }

    # my_list_parenthesi: list[str] = [par for par in s]
    
    
    # for key, val in my_dict.items():
    #     if s == "":
    #         return True
    #     if key in my_list_parenthesi and val in my_list_parenthesi:
    #         return True
    #     else:
    #         return False



    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    
    if len(s) == 0:
        return True
    else:
        return False
        
            
    # return my_list_parenthesi        
    # my_list_parenthesi: list[str] = [par for par in s]
    # parentesi: str = ""
    # for l in my_list_parenthesi:
    #     if l == "(" or l == "[" or l == "{":
    #         parentesi += l
    #     elif l == ")" or l == "]" or l == "}":
    #         parentesi += l

    # if parentesi == "()" or parentesi == "[]" or parentesi == "{}":
    #     return True
    # else:
    #     return False

print(is_valid_parenthesis("()[]{}"))