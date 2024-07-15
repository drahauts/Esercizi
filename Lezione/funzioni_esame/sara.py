def funzioncina(orario_inizio: float, orario_fine: float):
    paga: float = (orario_fine - orario_inizio) * 7

    return f'{paga:.2f}'

x, y = float(input('Orario inizio: ')), float(input('Orario fine: '))
print(funzioncina(x, y))
