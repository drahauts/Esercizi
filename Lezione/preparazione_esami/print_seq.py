"""
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51

Test:                               Result:
print_seq()
                                    Sequenza a):
                                    1
                                    2
                                    3
                                    4
                                    5
                                    6
                                    7
                                    Sequenza b):
                                    3
                                    8
                                    13
                                    18
                                    23
                                    Sequenza c):
                                    20
                                    14
                                    8
                                    2
                                    -4
                                    -10
                                    Sequenza d):
                                    19
                                    27
                                    35
                                    43
                                    51
"""


def print_seq(): 
    """
    a) 1, 2, 3, 4, 5, 6, 7
    """
    print("Sequenza a):")
    print(*range(1, 8), sep="\n")

    """
    b) 3, 8, 13, 18, 23
    """
    
    print("\nSequenza b):")

    print(*range(3, 24, 5), sep="\n")

    # c) 20, 14, 8, 2, -4, -10
    print("\nSequenza c):")
    print(*range(20, -11, -6), sep="\n")

    # d) 19, 27, 35, 43, 51
    print("\nSequenza d):")
    print(*range(19, 52, 8), sep="\n")
    
    

print_seq()

