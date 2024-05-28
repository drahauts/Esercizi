def remove_duplicates(my_list: list):
    my_set: set = set()
    no_dupl: list = []
    for l in my_list:
        if l not in my_set:
            my_set.add(l)
            no_dupl.append(l)

    return no_dupl

print(remove_duplicates([1,2,2,3,1,4,2,"a", "b", "a", 4,4,4]))