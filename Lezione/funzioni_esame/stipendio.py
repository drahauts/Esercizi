def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate < 40:
        return ore_lavorate * 10
    else:
        return 400 + (ore_lavorate - 40) * 15
    

print(calcola_stipendio(45))