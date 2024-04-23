"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list,
and then use a for loop to print the name of each pizza.
    • Modify your for loop to print a sentence using the name of the pizza, instead of printing just
    the name of the pizza. For each pizza, you should have one line of output containing a simple statement like
    I like pepperoni pizza.
    • Add a line at the end of your program, outside the for loop, that states how much you like pizza.
    The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence,
    such as I really love pizza!
"""

frase: list[str] = ["Il salame piccante", "Il prosciutto cotto con la mozarella", "Il gusto di funghi e salsiccia con mozarella che si scoglie"]
favorite_pizza: list[str] = ["Diavola", "Calzone", "Boscaiola"]
for f, pizza in zip(frase, favorite_pizza):
    print(f"In pizza {pizza} mi piace {f}")

print("I really love pizza!")


"""
4-2. Animals: Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
    • Modify your program to print a statement about each animal, such as A dog would make a great pet.
    • Add a line at the end of your program, stating what these animals have in common. You could print a
    sentence, such as Any of these animals would make a great pet!
"""

animals: list[str] = ["Delfini", "Pipistrelli", "Pinguini"]
facts: list[str] = ["utilizzano l'ecolocazione per navigare e individuare le prede.", "sono noti per il loro comportamento sociale.", "hanno una colonna vertebrale, che gli rende vertebrati."]

for animal, fact in zip(animals, facts):
    print(f"{animal} {fact}")
print("Tutti e tre gli animali sono a sangue caldo, il che significa che possono regolare la temperatura corporea internamente.")


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for i in range(1, 21):
    print(i)

# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.

# one_million: list[int] = [print(i)for i in range(1, 1000001)]


# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max()
# to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see
# how quickly Python can add a million numbers.
somma: list[int] = []
[somma.append(i)for i in range(1, 1000001)]

print(min(somma), max(somma))

print(f"La somma di un millione elementi è: {sum(somma)}")


# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.

for i in range(1, 21, 2):
    print(i)


# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

multiple: list[int] = []
[multiple.append(i)for i in range(3, 31, 3)]
print(multiple)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubes: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in cubes:
    print(i**3)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes: list[int] = [print(i**3)for i in range(1, 11)]

# for cube in cubes:
#     print(cube)
