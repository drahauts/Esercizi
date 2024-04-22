def move_zeroes(nums:list[int]) -> int:
    """
    Data una lista nums di interi, spostare gli zeri alla fine di questa lista
    mantenendo l'ordine originale dei numeri che non sono zeri

    Esempio 1:
    nums = [0, 1, 0, 3, 12] -> modificare la lista in [1, 3, 12, 0, 0]

    Esempio 2:
    nums = [0] -> la modifica e nulla perche abbiamo uno zero che non si sposta
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            x = nums.pop(i)
            nums.append(x)
    return nums

nums = [1, 0, 3, 0, 12]
print(move_zeroes(nums))