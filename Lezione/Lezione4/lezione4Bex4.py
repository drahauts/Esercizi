def majority_element(nums:list[int]) -> int:
    for i in nums:
        if nums.count(i) > len(nums) / 2:
            print(i)
            return i
    
    return None

    """
    Data una lista nums di n elementi, restituire l'elemento che
    compare piu n/2 volte.

    Esempio 1:
    nums = [3, 2, 3] -> restituire 3

    Esempio 2:
    nums = [2, 2, 1, 1, 1, 2] -> restituire None
    """
    # frequenza = {}
    # n = len(nums)
    # for num in nums:
    #     frequenza[num] = frequenza.get(num, 0) + 1  
    
    # for key, value in frequenza.items():
    #     if value > n / 2:
    #         return key
        
    # return None


# def majority_element(nums):
#     nums.sort()
#     print(nums)
#     majority_count = len(nums) // 2
#     for i in range(len(nums) - majority_count):
#         if nums[i] == nums[i + majority_count]:
#             return nums[i]
#     return None


nums = [2, 3, 3]
print(majority_element(nums)) 
