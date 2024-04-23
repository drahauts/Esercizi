# Exercise N.1

def subtract(x: float, y: float):
    print(f"Our x = {x} and our y = {y}")
    return x - y

x: float = float(input("Insert your first number: "))
y: float = float(input("Insert your second number: "))

print(subtract(x, y))

# Exercise N.2

"""
Exercise 1
Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller,
or equal to 5
"""

def check_value(n, m):
    if n > m:
        print(f"{n} è piu grande di {m}")
    elif n < m:
        print(f"{n} è piu piccolo di {m}")
    else:
        print(f"{n} è equevale a {m}")
   
n: float = float(input("Inserisci un numero: "))
m: float = float(input("Inserisci secondo numero: "))
check_value(n, m)

"""
Exercise 2
Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10
characters
"""

def check_length(s1: str):
    if len(s1) > 10:
        print(f"La tua parola {s1} contiene {len(s1)} caratteri ed è piu grande di 10 caratteri.")
    elif len(s1) < 10:
        print(f"La tua parola {s1} contiene {len(s1)} caratteri ed è piu piccolo di 10 caratteri.")
    else:
        print(f"La tua parola {s1} contiene {len(s1)} caratteri ed è equivale a 10 caratteri")


s1: str = str(input("Scrivi una parola: "))
check_length(s1)

"""
Exercise 3
Write a function print_numbers(), which takes a list of numbers as argument.
Using a for loop, print each number one by one.
"""

def print_numbers(l: list):
    for i in l:
        print(i)

print_numbers([1, 2, 3])


"""
Exercise 4
Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5,
and “equal” if it’s equal to 5
"""

def check_each(l: list):
    for i in l:
        if i > 5:
            print(f"{i} e maggiore di 5")
        elif i < 5:
            print(f"{i} è minore di 5")
        else:
            print(f"{i} è equivale a 5")


check_each([4, 23, 5, 7, 13, 65])


"""
Exercise 5
Write a function add_one(). It takes an integer as argument. The function adds 1 to
the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.

Example:
add_one_to_list([1, 2, 3])
outtput >>> [2, 3, 4]
"""

def add_one(n: int):
    return n + 1

print(add_one(12))

def add_one_to_list(l: list[int]) -> list[int]:
    new_list: list = []
    for i in l:
        new_list.append(add_one(i))
    print(new_list)

add_one_to_list([10, 12, 14])