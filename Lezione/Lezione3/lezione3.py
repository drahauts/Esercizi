"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza.
tore these pizza names in a list,
and then use a for loop to print the name of each pizza.
    • Modify your for loop to print a sentence using the name of the pizza,
    instead of printing just the name of the pizza. For each pizza, you
    should have one line of output containing a simple statement like
    I like pepperoni pizza.
    • Add a line at the end of your program, outside
    the for loop, that states how much you like pizza.
    The output should consist of three or more
    lines about the kinds of pizza you like and then an additional sentence,
    such as I really love pizza!
"""

frase: list[str] = ["Il salame piccante", "Il prosciutto è la mozarella",
                    "I funghi e salsiccia con mozarella che si scoglie"]
favorite_pizza: list[str] = ["Diavola", "Calzone", "Boscaiola"]
for f, pizza in zip(frase, favorite_pizza):
    print(f"In pizza {pizza} mi piace {f}")

print("I really love pizza!")


"""
4-2. Animals: Think of at least three different
animals that have a common characteristic.
Store the names of these animals in a list,
and then use a for loop to print out the name of each animal.
    • Modify your program to print a statement
    about each animal, such as A dog would make a great pet.
    • Add a line at the end of your program, stating
    what these animals have in common. You could print a
    sentence, such as Any of these animals would make a great pet!
"""

animals: list[str] = ["Delfini", "Pipistrelli", "Pinguini"]
facts: list[str] = ["utilizzano l'ecolocazione per navigare e individuare le prede.",
                    "sono noti per il loro comportamento sociale.", "hanno una colonna vertebrale, che gli rende vertebrati."]

for animal, fact in zip(animals, facts):
    print(f"{animal} {fact}")
print("Tutti e tre animali sono a sangue caldo, il che significa che possono regolare la temperatura corporea internamente.")


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


"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
"""


my_list1: list[str] = ["Roma", "Napoli", "Bari", "Milano", "Acilia"]
print(f"The first three items in the list are: {my_list1[0:3]}")
middle_index = len(my_list1) // 2
for item in my_list1[middle_index:middle_index + 3]:
    print(item)
print(f"The last three items in the list are: {my_list1[-3::]}")


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s
# favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate lis

# frase: list[str] = ["Il salame piccante", "Il prosciutto cotto con la mozarella", "Il gusto di funghi e salsiccia con mozarella che si scoglie"]
# favorite_pizza: list[str] = ["Diavola", "Calzone", "Boscaiola"]
# for f, pizza in zip(frase, favorite_pizza):
#     print(f"In pizza {pizza} mi piace {f}")

# print("I really love pizza!")

friend_pizzas: list[str] = favorite_pizza.copy()
print(friend_pizzas)

new_pizza: str = "Margherita"
favorite_pizza.append(new_pizza)
print(favorite_pizza)
friend_pizzas.append(new_pizza)

for my in favorite_pizza:
    print(f"My favourite pizza are: {my}")

for my_friend in friend_pizzas:
    print(f"My friend’s favorite pizzas are: {my_friend}")


"""
4-12. More Loops: All versions of foods.py in this section have avoided using for
loops when printing, to save space. Choose a version of foods.py, and write two
for loops to print each list of foods.
"""

print("Per tutti programmi ho usato il ciclo for!!! ")

"""
4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008.
You won’t use much of it now, but it might be interesting to skim through it.
"""
print("👍👍👍👍👍👍👍👍👍👍👍👍👍👍")

"""
4-15. Code Review: Choose three of the programs you’ve
written in this chapter and modify each one to comply with PEP 8.
"""

print("ho installato flake8, e la maggior parte di 'errori' me gli da per i commenti :( e non mi va di fare new line nei commenti, sorry:(, anche questa riga e piu di 79 charatteri, 1 errore in piu...")

"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""

"""
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Внимательно изучите ваши результаты и убедитесь, что вы понимаете, почему каждая строка оценивается как True или False.
• Создайте как минимум 10 тестов. Должно быть как минимум 5 тестов, которые оцениваются как True, и еще 5 тестов, которые оцениваются как False.
"""

car: str = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nIs car != 'ford'? I predict True.")
print(car != 'ford')
print("\nIs car.lower() == 'Subaru'.lower()? I predict True.")
print(car.lower() == "Subaru".lower())
print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)
print("\nIs car.isdigit()? I predict False.")
print(car.isdigit())


"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""


"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""

alien_color: str = "yellow"

if alien_color == "green":
    print("Congratulations, you just earned 5 points!!!")


"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
"""
alien_color: str = "red"

if alien_color == "green":
    print("Congratulations, you just earned 5 points!!!")
else:
    print("Congratulations, you just earned 10 points!!!")

"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

if alien_color == "green":
    print("Congratulations, you just earned 5 points!!!")
elif alien_color == "yellow":
    print("Congratulations, you just earned 10 points!!!")
else:
    print("Congratulations, you just earned 15 points!!!")

"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
"""

age: int = int(input("How ald are you? "))

if age < 2:
    print("That person is a baby.")
elif 2 < age <= 4:
    print("That person is a toddler.")
elif 4 < age <= 13:
    print("That person is a kid.")
elif 13 < age <= 20:
    print("That person is a teenager.")
elif 20 < age <= 65:
    print("That person is an adult.")
else:
    print("That the person is an elder")

"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
    • Make a list of your three favorite fruits and call it favorite_fruits.
    • Write five if statements. Each should check whether a certain kind of fruit is in your list.
      If the fruit is in your list, the if block should print a statement, such as You really like Apples!
"""

favorite_fruits: list[str] = ["Ananas", "Apple", "Watermelon"]

if "Banane" in favorite_fruits:
    print("You like banane")
if "Kiwi" in favorite_fruits:
    print("You don't like apple.")
if "Apple" in favorite_fruits:
    print(f"You liked {favorite_fruits[1]}")
if "Watermelon" in favorite_fruits:
    print(f"You liked {favorite_fruits[2]}")
if "Melone" in favorite_fruits:
    print("You dont like Melone!")

"""
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log in
to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
"""

usernames: list[str] = ["bratbrat", "admin", "pinston09", "ohdanila", "king1"]

for user in usernames:
    if user == "admin":
        print(f"Hello {user}, would you like to see a status report?")
    elif user != "admin":
        print(f"Hello {user}, thank you for logging in again")

"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
"""
usernames.clear()

if len(usernames) == 0:
    print("We need to find some users!")
else:
    for user in usernames:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        elif user != "admin":
            print(f"Hello {user}, thank you for logging in again")

"""
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
    • Make a list of five or more usernames called current_users.
    • Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
    • Loop through the new_users list to see if each new username has already been used.
      If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
    • Make sure your comparison is case insensitive. If 'John' has been used,
      'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
"""

current_users: list[str] = ["erfalcone99", "matador7", "cetriolino", "figota", "miniman"]
new_users: list[str] = ["bleedlucy", "qwerty", "mAtAdor7", "pemoluxx", "miniman"]

current_users_lower: list[str] = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user}, you need to enter a new username.")
    else:
        print(f"{user} that the username is available.")


