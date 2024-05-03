def even_odd_pattern(nums:list[int]) -> list[int]:
    lista_pari: list[int] = []
    lista_dispari: list[int] = []
    
    for num in nums:
        if num % 2 == 0:
            lista_pari.append(num)
        else:
            lista_dispari.append(num)

    return lista_pari + lista_dispari
    

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))
print(even_odd_pattern([3, 6, 1, 8, 4, 7, -1]))	
print(even_odd_pattern([3, 6, 1, 8, 4, 7, 0, -1]))
print(even_odd_pattern([3, 6, 18, 1, 8, 4, 7, 0, -1]))
print(even_odd_pattern([1]))