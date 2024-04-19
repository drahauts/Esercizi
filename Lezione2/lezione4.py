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

def check_value(n):
    if n > 5:
        print(f"{n} è piu grande di 5")
    elif n < 5:
        print(f"{n} è piu piccolo di 5")
    else:
        print(f"{n} è equevale a 5")
   
n: float = float(input("Inserisci un numero: "))
check_value(n)

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

print_numbers([1, 2, 3, 4, 5, 6, 7])


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